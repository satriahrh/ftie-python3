# Resolving Known Plaintext Attack on FTIE-RT-ACM
This repository means to be a remote repository for any code on a research of **Resolving Known Plaintext Attack on FTIE-RT-ACM**.
This research actually is my final project in pursuing the bachelor of [Informatics Engineering at Universitas Telkom](http://bif.telkomuniversity.ac.id/).

## Project Link
I made the project log available from Research Gate using the following link
> https://www.researchgate.net/project/Resolving-Known-Plaintext-Attack-on-FTIE-RT-ACM

## Research Proposal Abstract
[File to Image Encryption (FTIE-RT-ACM)](https://www.researchgate.net/publication/320087595_File_To_Image_Encryption_FTIE_Menggunakan_Algoritma_Randomized_Text_Dan_Arnold_Cat_Map_ACM_Untuk_Keamanan_Transmisi_Data_Digital) technique that makes use of
[Randomized Text algorithm (RT)](https://s3.amazonaws.com/academia.edu.documents/46998494/Randomized_Text_Encryption_a_New_Dimensi20160704-24345-9laysm.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1515661445&Signature=GGievOHY%2FRvQcBoILP5nWSizts0%3D&response-content-disposition=inline%3B%20filename%3DRandomized_Text_Encryption_a_New_Dimensi.pdf)
and [Arnold Cat Map algorithm (ACM)](https://en.wikipedia.org/wiki/Arnold%27s_cat_map)
have a weakness in RT algorithm block and ACM algorithm block.
Known plaintext attack that exploits a simple decryption equation
in RT algorithm block can be applied to generate the key used in the encryption.
This is could be done by FTIE-RT-ACM technique specifically in algorithm RT block
that does not implement a keystream generator, that in term of encryption it is useful
to keep the key safe.
Furthermore, the use of ACM 1D algorithm in ACM algorithm block has no proof of correctness.

This research proposes FTIE-RT-ACM technique implement keystream generator in
RT algorithm block and ACM 2D in the ACM algorithm block.
The keystream generator that will be used is [Blum Blum Shub (BBS) keystream generator algorithm](https://en.wikipedia.org/wiki/Blum_Blum_Shub).
BBS proved that it is not easy to predict given polynomial time.
Furthermore, the use of ACM 2D algorithm instead of ACM 1D algorithm gives more guarantee of
the algorithm correctness.

## Research Proposal in Indonesian
For you who willing to know more about my research, I have already done the research proposal available in Indonesia only (sad).
Not an Indonesian, just drop a request and I will work on it :D.
The research proposal then available by contacting me (DM, tweet, mention or anything) via Twitter: [@SatriaHRHarsono](https://twitter.com/SatriaHRHarsono).

## System Block Diagram
![System Block Diagram](docs/assets/system-block-diagram.png)

## Requirements
- `python==3.6.4`
- `nose==1.3.7`
- `pylint==1.8.2`
- other requirements will be written soon.

## Run The Project
Unfortunately, this project is not yet ready for production.
But some of its units are available and tested through command `nosetests`.

Documentation of each unit is not ready yet too and we are working on it :D

## Help
And yes, I am begging for your help. Just making an issue is ok tho.
