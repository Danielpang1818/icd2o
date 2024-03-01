N = int(input())
bidder_list = []
bid_list = []
for i in range(0,N):
    bidder = input()
    bid = int(input())
    bidder_list.append(bidder)
    bid_list.append(bid)
    biggest = max(auction_list)
    print (bidder[biggest])
    

