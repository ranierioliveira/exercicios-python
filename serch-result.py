def verify_votes(votes):
    vote_count = {}
    
    for vote in votes:
        if vote in vote_count: #verifies if vote is a key of vote_count
            vote_count[vote] +=1
        else:
            vote_count[vote] = 1
    print(vote_count)        
    
votes = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]
verify_votes(votes)