import logging
from abc import abstractmethod
from collections import defaultdict

from typing import (
    Dict, Iterator, List, Optional, Type, Union, Any, Iterable,
    TypeVar, DefaultDict, Set)
from nlp.pipeline.data.ontology import (
    Entry, EntryType, Annotation, Span, Link, Group)

logger = logging.getLogger(__name__)

__all__ = [
    "BasePack",
    "BaseMeta",
    "InternalMeta",
    "BaseIndex",
    "PackType"
]


class BaseMeta:
    """
    Basic Meta information for both DataPack and MultiPack.
    """
    def __init__(self, doc_id: Optional[str] = None):
        self.doc_id = doc_id
        self.process_state = ''
        self.cache_state = ''


class BaseIndex:
    """
    A set of indexes used in a datapack: (1) :attr:`entry_index`,
    the index from each tid to the corresponding entry;
    (2) :attr:`type_index`, the index from each type to the entries of that
    type; (3) :attr:`component_index`, the index from each component to the
    entries generated by that component; (4) :attr:`link_index`, the index
    from child (:attr:`link_index["child_index"]`)and parent
    (:attr:`link_index["parent_index"]`) nodes to links; (5)
    :attr:`group_index`, the index from group members to groups.
    """

    def __init__(self, data_pack):
        self.data_pack: BasePack = data_pack
        # basic indexes (switches always on)
        self.entry_index: Dict[str, Entry] = dict()
        self.type_index: DefaultDict[Type, Set[str]] = defaultdict(set)
        self.component_index: DefaultDict[str, Set[str]] = defaultdict(set)
        # other indexes (built when first looked up)
        self._group_index = defaultdict(set)
        self._link_index: Dict[str, DefaultDict[str, set]] = dict()
        # indexing switches
        self._group_index_switch = False
        self._link_index_switch = False

    @property
    def link_index_switch(self):
        return self._link_index_switch

    def turn_link_index_switch(self, on: bool):
        self._link_index_switch = on

    @property
    def group_index_switch(self):
        return self._group_index_switch

    def turn_group_index_switch(self, on: bool):
        self._group_index_switch = on

    def link_index(self, tid: str, as_parent: bool = True) -> Set[str]:
        """
        Look up the link_index with key ``tid``.

        Args:
            tid (str): the tid of the entry being looked up.
            as_parent (bool): If `as_patent` is True, will look up
                :attr:`link_index["parent_index"] and return the tids of links
                whose parent is `tid`. Otherwise,  will look up
                :attr:`link_index["child_index"] and return the tids of links
                whose child is `tid`.
        """
        if not self._link_index_switch:
            self.update_link_index(self.data_pack.links)
        if as_parent:
            return self._link_index["parent_index"][tid]
        else:
            return self._link_index["child_index"][tid]

    def group_index(self, tid: str) -> Set[str]:
        """
        Look up the group_index with key `tid`.
        """
        if not self._group_index_switch:
            self.update_group_index(self.data_pack.groups)
        return self._group_index[tid]

    def in_span(self,
                inner_entry: Union[str, Entry],
                span: Span) -> bool:
        """Check whether the ``inner entry`` is within the given ``span``.
        Link entries are considered in a span if both the
        parent and the child are within the span. Group entries are
        considered in a span if all the members are within the span.

        Args:
            inner_entry (str or Entry): An :class:`Entry` object to be checked.
                We will check whether this entry is within ``span``.
            span (Span): A :class:`Span` object to be checked. We will check
                whether the ``inner_entry`` is within this span.
        """

        if isinstance(inner_entry, str):
            inner_entry = self.entry_index[inner_entry]

        if isinstance(inner_entry, Annotation):
            inner_begin = inner_entry.span.begin
            inner_end = inner_entry.span.end
        elif isinstance(inner_entry, Link):
            child = inner_entry.get_child()
            parent = inner_entry.get_parent()
            inner_begin = min(child.span.begin, parent.span.begin)
            inner_end = max(child.span.end, parent.span.end)
        elif isinstance(inner_entry, Group):
            inner_begin = -1
            inner_end = -1
            for mem in inner_entry.get_members():
                if inner_begin == -1:
                    inner_begin = mem.span.begin
                inner_begin = min(inner_begin, mem.span.begin)
                inner_end = max(inner_end, mem.span.end)
        else:
            raise ValueError(
                f"Invalid entry type {type(inner_entry)}. A valid entry "
                f"should be an instance of Annotation, Link, or Group."
            )
        return inner_begin >= span.begin and inner_end <= span.end

    def have_overlap(self,
                     entry1: Union[Annotation, str],
                     entry2: Union[Annotation, str]) -> bool:
        """Check whether the two annotations have overlap in span.

        Args:
            entry1 (str or Annotation): An :class:`Annotation` object to be
                checked, or the tid of the Annotation.
            entry2 (str or Annotation): Another :class:`Annotation` object to be
                checked, or the tid of the Annotation.
        """
        if isinstance(entry1, str):
            e = self.entry_index[entry1]
            if not isinstance(e, Annotation):
                raise TypeError(f"'entry1' should be an instance of Annotation,"
                                f" but get {type(e)}")
            entry1 = e

        if not isinstance(entry1, Annotation):
            raise TypeError(f"'entry1' should be an instance of Annotation,"
                            f" but get {type(entry1)}")

        if isinstance(entry2, str):
            e = self.entry_index[entry2]
            if not isinstance(e, Annotation):
                raise TypeError(f"'entry2' should be an instance of Annotation,"
                                f" but get {type(e)}")
            entry2 = e

        if not isinstance(entry2, Annotation):
            raise TypeError(f"'entry2' should be an instance of Annotation,"
                            f" but get {type(entry2)}")

        return not (entry1.span.begin >= entry2.span.end or
                    entry1.span.end <= entry2.span.begin)

    def update_basic_index(self, entries: List[Entry]):
        """Build or update the basic indexes, including (1) :attr:`entry_index`,
        the index from each tid to the corresponding entry;
        (2) :attr:`type_index`, the index from each type to the entries of that
        type; (3) :attr:`component_index`, the index from each component to the
        entries generated by that component.

        Args:
            entries (list): a list of entires to be added into the basic index.
        """
        for entry in entries:
            self.entry_index[entry.tid] = entry
            self.type_index[type(entry)].add(entry.tid)
            self.component_index[entry.component].add(entry.tid)

    def update_link_index(self, links: List[Link]):
        """Build or update :attr:`link_index`, the index from child and parent
        nodes to links. :attr:`link_index` consists of two sub-indexes:
        "child_index" is the index from child nodes to their corresponding
        links, and "parent_index" is the index from parent nodes to their
        corresponding links.

        Args:
            links (list): a list of links to be added into the index.
        """
        logger.debug("Updating link index")
        if not self.link_index_switch:
            self.turn_link_index_switch(on=True)
            self._link_index["child_index"] = defaultdict(set)
            self._link_index["parent_index"] = defaultdict(set)
            links = self.data_pack.links

        for link in links:
            self._link_index["child_index"][link.child].add(link.tid)
            self._link_index["parent_index"][link.parent].add(link.tid)

    def update_group_index(self, groups: List[Group]):
        """Build or update :attr:`group_index`, the index from group members
         to groups.

        Args:
            groups (list): a list of groups to be added into the index.
        """
        logger.debug("Updating group index")
        if not self.group_index_switch:
            self.turn_group_index_switch(on=True)
            self._group_index = defaultdict(set)
            groups = self.data_pack.groups

        for group in groups:
            for member in group.members:
                self._group_index[member].add(group.tid)


class InternalMeta:
    """
    The internal meta information of **one kind of entry** in a datapack.
    Note that the :attr:`intertal_metas` in :class:`BasePack` is a dict in
    which the keys are entries types and the values are objects of
    :class:`InternalMeta`.
    """
    def __init__(self):
        self.id_counter = 0
        self.fields_created = defaultdict(set)
        self.default_component = None


class BasePack:
    """
    The base class of DataPack and MultiPack
    """
    def __init__(self, doc_id: Optional[str] = None):
        self.links: List[Link] = []
        self.groups: List[Group] = []

        self.meta: BaseMeta = BaseMeta(doc_id)

        self.index: BaseIndex = BaseIndex(self)
        self.internal_metas: \
            Dict[type, InternalMeta] = defaultdict(InternalMeta)

    def set_meta(self, **kwargs):
        for k, v in kwargs.items():
            if not hasattr(self.meta, k):
                raise AttributeError(f"Meta has no attribute named {k}")
            setattr(self.meta, k, v)

    @abstractmethod
    def add_entry(self, entry: EntryType) -> EntryType:
        """
        Force add an :class:`Entry` object to the :class:`BasePack` object.
        Allow duplicate entries in a pack.

        Args:
            entry (Entry): An :class:`Entry` object to be added to the pack.

        Returns:
            The input entry itself
        """
        raise NotImplementedError

    @abstractmethod
    def add_or_get_entry(self, entry: EntryType) -> EntryType:
        """
        Try to add an :class:`Entry` object to the :class:`DataPack` object.
        If a same entry already exists, will return the existing entry
        instead of adding the new one. Note that we regard two entries to be
        same if their :meth:`eq` have the same return value, and users could
        override :meth:`eq` in their custom entry classes.

        Args:
            entry (Entry): An :class:`Entry` object to be added to the pack.

        Returns:
            If a same entry already exists, returns the existing
            entry. Otherwise, return the (input) entry just added.
        """
        raise NotImplementedError

    @abstractmethod
    def record_fields(self, fields: List[str], entry_type: Type[Entry],
                      component: Optional[str]):
        """Record in the internal meta that ``component`` has generated
        ``fields`` for ``entry_type``.

        If ``component`` is None, we will record fields for all existing
        component.
        """
        raise NotImplementedError

    @abstractmethod
    def get_data(
            self,
            context_type: str,
            requests: Optional[Dict[Type[Entry], Union[Dict, List]]] = None,
            offset: int = 0
    ) -> Iterator[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def get_entries(self,
                    entry_type: Type[EntryType],
                    range_annotation: Optional[Annotation] = None,
                    components: Optional[Union[str, List[str]]] = None
                    ) -> Iterable[EntryType]:
        """
        Get ``entry_type`` entries from the span of ``range_annotation`` in a
        DataPack.

        Args:
            entry_type (type): The type of entries requested.
            range_annotation (Annotation, optional): The range of entries
                requested. If `None`, will return valid entries in the range of
                whole data_pack.
            components (str or list, optional): The component generating the
                entries requested. If `None`, will return valid entries
                generated by any component.
        """
        raise NotImplementedError

    def get(self,
            entry_type: Type[EntryType],
            range_annotation: Optional[Annotation] = None,
            component: Optional[str] = None) -> Iterable[EntryType]:
        return self.get_entries(entry_type, range_annotation, component)


PackType = TypeVar('PackType', bound=BasePack)
