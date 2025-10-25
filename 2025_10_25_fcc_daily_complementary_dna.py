# Complementary DNA
# Given a string representing a DNA sequence, return its complementary strand using the following rules:

# DNA consists of the letters "A", "C", "G", and "T".
# The letters "A" and "T" complement each other.
# The letters "C" and "G" complement each other.
# For example, given "ACGT", return "TGCA".

def complementary_dna(strand: str) -> str:
    # Define the mapping table: ACTG -> TGAC
    from_bases = "ACTG"
    to_bases = "TGAC"
    translation_table = str.maketrans(from_bases, to_bases)
    # Apply single-pass translation
    return strand.translate(translation_table)
    

if __name__ == "__main__":
    # Test 1 should return "TGCA".
    print(complementary_dna("ACGT"))
    # Test 2 should return "TACGCATGCAATCG".
    print(complementary_dna("ATGCGTACGTTAGC"))
    # Test 3 should return "CCGAATGCTAGCTTC".
    print(complementary_dna("GGCTTACGATCGAAG"))
    # Test 4 should return "CTAGATCGATCCGATCGATC"
    print(complementary_dna("GATCTAGCTAGGCTAGCTAG"))