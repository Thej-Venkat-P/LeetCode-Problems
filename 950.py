# url: https://leetcode.com/problems/reveal-cards-in-increasing-order/
    
    
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        def order(deck):
            if len(deck) <= 1:
                return deck
            n = len(deck)
            if n & 1 == 1:
                mid = n//2 + 1
                main_deck = deck[:mid]
                side_deck = order(deck[mid:])
                side_deck = [side_deck[-1]] + side_deck[:-1]
                ans = []
                for i in range(mid-1):
                    ans.append(main_deck[i])
                    ans.append(side_deck[i])
                ans.append(main_deck[-1])
                return ans
            else:
                mid = n//2
                main_deck = deck[:mid]
                side_deck = order(deck[mid:])
                ans = []
                for i in range(mid):
                    ans.append(main_deck[i])
                    ans.append(side_deck[i])
                return ans
        return order(deck)
    
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0]*n
        dq=collections.deque(range(n))
        for card in deck:
            ans[dq.popleft()] = card
            if dq:
                dq.append(dq.popleft())
        return ans

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        dq=collections.deque()
        for card in reversed(sorted(deck)):
            dq.rotate()
            dq.appendleft(card)
        return list(dq)