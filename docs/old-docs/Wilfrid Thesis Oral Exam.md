# Prof. Ray
1. p. 13, Define the parameters clearly and link them to the figures.
2. Change 'gNB Active' to 'gNB send on-demand SIB1' (figure out the correct name for the corresponding state)
3. p. 25, i is an index of time (or, the timing of the RO)
4. Define the RO before using it.
5. p. 28, Show us the length of Ta directly on the timing diagram
6. p. 29, show us the Eq. that you referred from [13] and then you can tell us how do you approximate it to devive the Eq. (4)
7. p. 30 What is the value of 𝜂? What is the unit of distance (𝑑?) in p.30
8. p. 32, Does the Eq. apply to both OAI and srsRAN gNB?
9. p. 35, Do you test your results on srsRAN?
10. p. 36~: give a quick summary for each figure
11. p. 41, we may measure the power consumption of gNB which only transmit SIB 1.
12. What is the unit of the pathloss formula? From the paper, it should be m or km. In your thesis, it's cm. Does it work?
13. How can we use your model?

# Prof. Hsu
1. RACH is only a wake up signal. The ES gNB will transmit on-demand SIB1 after receiving the wake up signal. It will NOT move the active state. Please check the spec. and revise your thesis/paper accordingly.
2. p. 10/15, the state transition diagram of NES needs to be revisited. Its fundamental to know that a controlled based on traffic load can change the gNB's traffic can wake-up the gNB, not UE.
3. p. 26, can you explain srsRAN set 𝛽=0? Does your Msg1 attacker work on srsRAN (𝛽=0)?
4. Show us how do you modify the gNB to get your results.
5. p. 75, show 𝑘 on your figure

# Prof. TY
1. Use flowchart with more details to show your design. You can refer to 3GPP spec for the details
2. How do you make sure your attacker work on real gNB?
3. p. 26, Show us your contribution on your Eqs. How do you modify it? How do you verify it works? How/Why does it work? Give notes
4. How do you increase the jamming efficiency of your attacker? For example, copy the gNB's noise behavior and prevent from continuous jamming.
5. p. 31, consider the power consumption in different stage. gNB has different power consumption which depends on the number of serving UEs.
6. p. 42, the result is only one UE. What would be the power consumption in running different channels?

# Prof. RT
1. p. 29, 30, provide a summary of which Equations are proposed by you, which is an adaptation of original formula, which formula you just use from reference.
2. Test non-fixed preambleID. Will the result be the same as the current result?
