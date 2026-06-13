# Data Structures & Systems Design Assignment

# Overview

This repository contains solutions for the Software Engineering Intern assessment.

The assignment consists of:

1. LRU Cache Implementation
2. Event Scheduler
3. Complexity Analysis and Design Discussion

---

## Problem 1: LRU Cache

# Approach

The LRU Cache is implemented using:

Hash Map (Dictionary)
Doubly Linked List

The hash map provides O(1) access to cache entries, while the doubly linked list maintains the order of usage.

Whenever an item is accessed or updated, it is moved to the front of the list. When the cache reaches capacity, the least recently used item is removed.

# Complexity

| Operation | Time |
| --------- | ---- |
| get()     | O(1) |
| put()     | O(1) |

Space Complexity: O(capacity)

---

## Problem 2: Event Scheduler

# can_attend_all(events)

Events are sorted by start time and checked for overlaps.

Time Complexity: O(n log n)

# min_rooms_required(events)

A min heap is used to track active meetings and efficiently reuse available rooms.

Time Complexity: O(n log n)

Space Complexity: O(n)

---

# Trade-offs

A hash map and doubly linked list provide efficient lookup and ordering operations at the cost of additional memory.

---

# Future Improvements

The scheduler can be extended to assign actual room identifiers (Room A, Room B, etc.) by storing room information alongside end times in the heap.

---

# Concurrency

To make the LRU Cache thread-safe, synchronization mechanisms such as mutex locks or read-write locks can be introduced to protect cache operations.
