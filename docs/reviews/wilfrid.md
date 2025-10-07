# Taiwan University of Science and Technology Oral Test QA Wilfrid Azariah

## Prof. Ray
- [x] p. 13, Define the parameters clearly and link them to the figures.
    - The parameters definition is detailed in the reference. It was too long to explain them 1 by 1 during the oral-exam
- [x] Change 'gNB Active' to 'gNB send on-demand SIB1' (figure out the correct name for the corresponding state)
    - Currently we use `active` and `sleep` by 3GPP TR 138.864 definition in Technique A-3-2 (not Technique A-5), where:
        - `active` = 
            - Main receiver ON
            - WUS receiver OFF
        - `sleep` =
            - Main receiver OFF
            - WUS receiver ON
        - WUS from UE can change `sleep` to `active`
- [x] p. 25, i is an index of time (or, the timing of the RO)
    - Changed the definition
    <img width="252" height="126" alt="image" src="https://github.com/user-attachments/assets/f3fb565f-40e7-49b9-9c06-b082e7b1a5e1" />
- [x] Define the RO before using it.
    - Added explanation about RO
    <img width="505" height="240" alt="image" src="https://github.com/user-attachments/assets/83bf9598-5c7c-463f-8d61-0685221bd084" />
- [x] p. 28, Show us the length of Ta directly on the timing diagram
    - Added length of Ta and j directly on the timing diagram
    <img width="1031" height="676" alt="image" src="https://github.com/user-attachments/assets/7dfd30ad-4ba1-4783-a2e0-941c25df1c5c" />
- [x] p. 29, show us the Eq. that you referred from [13] and then you can tell us how do you approximate it to devive the Eq. (4)
    - The approximation is done empirically. The capture ratio curve resembles the sigmoidal "S-shaped" form. Added this explanation in thesis book.
    <img width="429" height="317" alt="image" src="https://github.com/user-attachments/assets/92a07c92-acb7-4fe0-8e48-228bedd90a6b" />
- [x] p. 30 What is the value of 𝜂? What is the unit of distance (𝑑?) in p.30
    - Value of n is the pathloss exponent that models the rate of loss of power. Typicall it is between 2 and 4 in urban cellular system.
    - unit of distance = cm
- [x] p. 32, Does the Eq. apply to both OAI and srsRAN gNB?
    - According to the new used WUS definition in Technique A-3-2 in 3GPP TR 138.864, this equation is no longer used
- [x] p. 35, Do you test your results on srsRAN?
    - Added figure 4.7 and 4.8 to explain how attacker can work on srsRAN with high Msg1 Power
    <img width="435" height="326" alt="image" src="https://github.com/user-attachments/assets/2a6ae86a-216a-4dfc-a9a4-70835e0c97c0" />
    <img width="434" height="322" alt="image" src="https://github.com/user-attachments/assets/1c1c4af7-6805-4d7a-8850-5877cd6745b5" />
- [x] p. 36: give a quick summary for each figure
    - Summary of each figure has been provided in the red box
    <img width="577" height="374" alt="image" src="https://github.com/user-attachments/assets/a1956599-49f3-4862-ae81-a35e738cc6a7" />
- [x] p. 41, we may measure the power consumption of gNB which only transmit SIB 1.
    - Measurement result show no difference of gNB power consumption with/without SIB1
- [x] What is the unit of the pathloss formula? From the paper, it should be m or km. In your thesis, it's cm. Does it work?
    - It works because the power calculated is relative to a reference power. If we use meter, then the reference power is in meter. Same applies in cm or km.
- [x] How can we use your model?
    - We can do testing to gather data (input = attacker parameter, output = msg2 from gNB). Using the data, we can estimate the parameter of gNB in the equation. Then, we can use the equation to calculate the attacker parameter for successfull attack
    - Added this part into Future Work section
    <img width="484" height="101" alt="image" src="https://github.com/user-attachments/assets/dc6dc6b1-a8f9-4273-ab6d-94cf94239287" />
- [x] Do more experiment to prove our attacker can successfully attack srsRAN gNB
    - Added figure 4.7 and 4.8 to explain how attacker can work on srsRAN with high Msg1 Power
    <img width="435" height="326" alt="image" src="https://github.com/user-attachments/assets/2a6ae86a-216a-4dfc-a9a4-70835e0c97c0" />
    <img width="434" height="322" alt="image" src="https://github.com/user-attachments/assets/1c1c4af7-6805-4d7a-8850-5877cd6745b5" />
- [x] Consider attacking OAI when attacker power is bigger than UE
    - To include this case on the equation, we add gNB type indicator variable and include this in the Msg1 Access Success Probability equation
    <img width="1039" height="276" alt="image" src="https://github.com/user-attachments/assets/928b42e9-e85c-4502-bc16-0875dbdec037" />

## Prof. Sheu
- [x] RACH is only a wake up signal. The ES gNB will transmit on-demand SIB1 after receiving the wake up signal. It will NOT move the active state. Please check the spec. and revise your thesis/paper accordingly.
    - Revised thesis. Currently we use `active` and `sleep` by 3GPP TR 138.864 definition in Technique A-3-2 (not Technique A-5), where:
        - `active` = 
            - Main receiver ON
            - WUS receiver OFF
        - `sleep` =
            - Main receiver OFF
            - WUS receiver ON
        - WUS from UE can change `sleep` to `active`
- [x] p. 10/15, the state transition diagram of NES needs to be revisited. Its fundamental to know that a controlled based on traffic load can change the gNB's traffic can wake-up the gNB, not UE.
    - Revised thesis. Currently we use `active` and `sleep` by 3GPP TR 138.864 definition in Technique A-3-2 (not Technique A-5), where:
        - `active` = 
            - Main receiver ON
            - WUS receiver OFF
        - `sleep` =
            - Main receiver OFF
            - WUS receiver ON
        - WUS from UE can change `sleep` to `active`
- [x] p. 26, can you explain srsRAN set 𝛽=0? Does your Msg1 attacker work on srsRAN (𝛽=0)?
    - Added figure 4.7 and 4.8 to explain how attacker can work on srsRAN with high Msg1 Power
    <img width="435" height="326" alt="image" src="https://github.com/user-attachments/assets/2a6ae86a-216a-4dfc-a9a4-70835e0c97c0" />
    <img width="434" height="322" alt="image" src="https://github.com/user-attachments/assets/1c1c4af7-6805-4d7a-8850-5877cd6745b5" />
- [x] Show us how do you modify the gNB to get your results.
    - The gNB and attacker modification is detailed in the thesis book. It was too long to explain them 1 by 1 during the oral-exam
- [x] p. 75, show 𝑘 on your figure
    - Added k in figure
    <img width="876" height="279" alt="image" src="https://github.com/user-attachments/assets/4d556bec-2044-4256-8f3d-6a7920c24b0f" />

## Prof. TY
- [x] Use flowchart with more details to show your design. You can refer to 3GPP spec for the details
    - Detailed flowcharts are provided inside the thesis book. It was too long to explain them 1 by 1 during the oral-exam
- [x] How do you make sure your attacker work on real gNB?
    - We can do testing to gather data (input = attacker parameter, output = msg2 from gNB). Using the data, we can estimate the parameter of gNB in the equation. Then, we can use the equation to calculate the attacker parameter for successfull attack
- [x] p. 26, Show us your contribution on your Eqs. How do you modify it? How do you verify it works? How/Why does it work? Give notes
    - Detailed explanation is provided inside the thesis book. It was too long to explain them 1 by 1 during the oral-exam
    - Added table 3.1 in thesis book to summarize the source of equations
    <img width="472" height="608" alt="image" src="https://github.com/user-attachments/assets/6b633152-e9c5-4c62-8685-0e09c500c2cc" />
- [x] How do you increase the jamming efficiency of your attacker? For example, copy the gNB's noise behavior and prevent from continuous jamming.
    - For Msg1 Attack on Network Access, continous jamming is required due to OAI gNB's historical algorithm for noise estimate
    - For Msg1 Attack on NES, jamming efficiency can be increased by copying the gNB's active period and only attack when gNB goes back to sleep.
- [x] p. 31, consider the power consumption in different stage. gNB has different power consumption which depends on the number of serving UEs.
    - We could not simulate power consumption at different stage based on number of UE
- [x] p. 42, the result is only one UE. What would be the power consumption in running different channels?
    - We could not simulate power consumption at different stage based on number of UE
    - We did some measurement of gNB power consumption with/without SIB1. Measurement result show no difference.

## Prof. RT
- [x] p. 29, 30, provide a summary of which Equations are proposed by you, which is an adaptation of original formula, which formula you just use from reference.
    - Added table 3.1 in thesis book to summarize the source of equations
    <img width="472" height="608" alt="image" src="https://github.com/user-attachments/assets/6b633152-e9c5-4c62-8685-0e09c500c2cc" />

- [x] Test non-fixed preambleID. Will the result be the same as the current result?
    - Yes, the result is the same
