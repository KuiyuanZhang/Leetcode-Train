class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到末尾，所以定义一个方法
    def move_node_to_tail(self, key):
            # 先将哈希表key指向的节点拎出来，为了简洁起名node
            #      hashmap[key]                               hashmap[key]
            #           |                                          |
            #           V              -->                         V
            # prev <-> node <-> next         pre <-> next   ...   node
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            # 之后将node插入到尾节点前
            #                 hashmap[key]                 hashmap[key]
            #                      |                            |
            #                      V        -->                 V
            # prev <-> tail  ...  node                prev <-> node <-> tail
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到末尾（变成最新访问的）
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到末尾
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 去掉哈希表对应项
                self.hashmap.pop(self.head.next.key)
                # 去掉最久没有被访问过的节点，即头节点之后的节点
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 如果不在的话就插入到尾节点前
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new



class DLinkedNode:
    """
    双链表节点
    """
    def __init__(self, key: int = 0, value: int = 0):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value
 
class LRUCache:
 
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
 
    def get(self, key: int) -> int:
        # 如果key不在cache中, 直接返回-1
        if key not in self.cache:
            return -1
        
        # 从cache中获取key对应的节点
        node = self.cache[key]
        # 移动节点到链表的头部
        self.move_to_head(node)
        # 返回节点的值
        return node.value
 
    def put(self, key: int, value: int) -> None:
        
        node = DLinkedNode(key, value)
 
        # 如果key不在cache中
        if key not in self.cache:
            # 且此时缓存容量已满
            if self.capacity == self.size:
                # 移除链表中最后一个节点
                last_node = self.remove_last()
                # 同时从cache中弹出最后一个节点
                self.cache.pop(last_node.key)
                # 把新节点加入到链表的头部
                self.add_to_head(node)
                # 更新cache
                self.cache[key] = node
            else:
                # 容量未满, 直接把新节点加入到链表头部                
                self.add_to_head(node)
                # 同时更新缓存
                self.cache[key] = node
                # 缓存大小加一
                self.size += 1
        else:
            # 如果key在cache中, 那就不用再考虑缓存容量的影响
            # 把老节点cache和链表中移除
            old_node = self.cache.pop(key)
            self.remove_node(old_node)
            # 再把新节点加入到cache和链表中
            self.add_to_head(node)
            self.cache[key] = node
 
    def add_to_head(self, node: DLinkedNode):
        """
        把节点加入到链表头部
        """
        next_node = self.head.next
 
        self.head.next = node
        node.prev = self.head
 
        node.next = next_node
        next_node.prev = node
    
    def remove_node(self, node: DLinkedNode):
        """
        从链表中移除指定节点
        """
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_head(self, node: DLinkedNode):
        """
        把节点移动到链表头部
        """
        self.remove_node(node)
        self.add_to_head(node)
    
    def remove_last(self) -> DLinkedNode:
        """
        移除链表中最后一个节点并返回
        """
        last_node = self.tail.prev
 
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return last_node
 