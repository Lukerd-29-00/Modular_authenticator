# modular arithmetic Zero-Knowledge proof: tonelli-shanks
This is a challenge that tests for basic number theory knowledge. You are given a number that has been raised to a power of two mod a prime and need to find a root in order to pass the proof.

## Solution
Check soln.py. The naive solution is to run tonelli shanks log2(e) times. This will probably take about a half hour or more at least. The better way is to find the number d where e * d = 2 mod phi, and then raise the given public key to d. Then you can simply take the square root once, which is much faster.

## Challenge files
the challenge should consist of public_key.json, gen_key.py, server.py, and server.sh (for local testing). server.sh should be running remotely.

## Notes
the solution should only take about 15 seconds.

## Challenge description
Alright, so I think I've got the basics of this zero-knowledge proof stuff down now. Care to take a gander?
