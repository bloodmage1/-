s1="""
GCGCGAACTTAAGTTAACCTATCCATGTCCTATGGAGTCAAAACTTGGTCCTCCCCAGAG
GCTGCATTGTAGCGTACCATAGCGATTGTGTTCGATGGCCCAATAACTATTTTTGGACAA
AATAGTCTAATCTAGGTTTCGCACCTATTTGTGTTGCAGGGCTTACCGTCAAACCCCTGT
CAACTCACTGCCATGCATCGGAGTTCACATGTACGTGCCAAAATCACGGCCAAAGGTGCT
ACAAGAAGGTTGCAATTTTTGGGTTTACTACCTCGGGCGACAGGGGGCTGTGTTCAGGTA
GCAATCTCAGCAAACATCATTGCGGGCCTTATCGTTGTGTGGTTTACATTAGTACACGCT
CGAGTTCAGGACTGGGTCAACTTCAATTAATTGCGGGGGGAGGCAATGGAATACATCAGG
AGCTCCTGCCTAGGGGGTATTTGACGGAAGTAGCACTGTGGCCGGAACCTGTGCAGCACA
CTCCTCGTTGAGACCATCTGCGCCGTCCTTCAGCAGGGGATTAATAGGCACGGAGGGAGA
TAGAAGGTTCAGTTCAACCATGAATTCGTCGTTCTGGCTAAGTAATACGTGCATGCTTGC
TTAGGGCTTTTGACGCGAGTGTAGCTATGATAATAAGCGTGGTAAAAGGGCAAATATCTA
TGTTCTTAGATTAGGAAATCTAATGAGTCGCGCTCCACGGGTCGCACAATTTTCGGACAG
CAGACATCGTCACGAACGAAATGAGGTGGAAAAATTCGACGTTGCCAATTTCGGATGACT
GCCTAGTGCTCTACGGTTGAAGCCGGCGTTCAGCGGCCTAGTTTCTTTTCGTCTACTTGG
GCGC
""".replace("\n","")

def reverse(s1):
    b= ""
    for i in s1:
        b = i+b
    b=b.replace("T","a")
    b=b.replace("C","g")
    b=b.replace("G","c")
    b=b.replace("A","t")
    b=b.upper()
    return b
s1=s1+"HHHHHHHHHHHH"
def sol(s1):
    for j in range(len(s1)-12):
        if s1[j:j+4] == reverse(s1[j:j+4]): 
            print(j+1, 4)
        if s1[j:j+6] == reverse(s1[j:j+6]):
            print(j+1, 6)
        if s1[j:j+8] == reverse(s1[j:j+8]):
            print(j+1, 8)
        if s1[j:j+10] == reverse(s1[j:j+10]):
            print(j+1, 10)
        if s1[j:j+12] == reverse(s1[j:j+12]):
            print(j+1, 12)       
sol(s1)