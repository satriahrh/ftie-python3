# Resolving Known Plaintext Attack on FTIE-RT-ACM
This repository mean to be a remote repository for any code on a research of **Resolving Known Plaintext Attack on FTIE-RT-ACM**.
This research actualy is my final project in pursuing bachelor of [Informatics Engineering at Universitas Telkom](http://bif.telkomuniversity.ac.id/).

## Project Link
I made the project log available from Research Gate using following link
> https://www.researchgate.net/project/Resolving-Known-Plaintext-Attack-on-FTIE-RT-ACM

## Research Proposal Abstract
[File to Image Encryption (FTIE-RT-ACM)](https://www.researchgate.net/publication/320087595_File_To_Image_Encryption_FTIE_Menggunakan_Algoritma_Randomized_Text_Dan_Arnold_Cat_Map_ACM_Untuk_Keamanan_Transmisi_Data_Digital) technique that make use of
[Randomized Text algoritm (RT)](https://s3.amazonaws.com/academia.edu.documents/46998494/Randomized_Text_Encryption_a_New_Dimensi20160704-24345-9laysm.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1515661445&Signature=GGievOHY%2FRvQcBoILP5nWSizts0%3D&response-content-disposition=inline%3B%20filename%3DRandomized_Text_Encryption_a_New_Dimensi.pdf)
and [Arnold Cat Map algorithm (ACM)](https://en.wikipedia.org/wiki/Arnold%27s_cat_map)
have a weakness in RT algorithm block and ACM algorithm block.
Known plaintext attack that exploits a simple decryption equation
in RT algorithm block can be applied to generate the key used in the encryption.
This is could be done by FTIE-RT-ACM technique specifically in algorithm RT block
that do not implement a keystream generator, that in term of encryption it is useful
to keep the key safe.
Furthermore the use of ACM 1D algorithm in ACM algorithm block has no proof of correctness.

This research propose FTIE-RT-ACM tehcnique implement keystream generator in
RT algorithm block and ACM 2D in the ACM algorithm block.
The keystream generator that will be used is [Blum Blum Shub (BBS) keysteram generator algorithm](https://en.wikipedia.org/wiki/Blum_Blum_Shub).
BBS proved that it is not easy to predict given polynomial time.
Furthermore the use of ACM 2D algoritm instead of ACM 1D algorithm gives more guarantee of
the algorithm correctness.

## Requirements
- `python==3.5.2`
- `nose==1.3.7`
- other requirements will be written soon.
