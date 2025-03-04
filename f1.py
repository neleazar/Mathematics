class F1VS:
    def __init__(self, elements):
        """
        Initialize the F1 vector space with a set of elements.
        Ensure that the base element 0 is included.
        """
        self.elements = set(elements)
        self.elements.add(0)  # Ensure 0 is included as the base element

    def __repr__(self):
        return f"F1VS({self.elements})"

    def subset(self, subset_elements):
        """
        Create a subset of the vector space.
        Ensure that the base element 0 is included in the subset.
        """
        subset = set(subset_elements)
        subset.add(0)  # Ensure 0 is included in the subset
        if not subset.issubset(self.elements):
            raise ValueError("Subset contains elements not in the original vector space.")
        return F1VS(subset)

    def direct_sum(self, other):
        """
        Compute the direct sum (disjoint union with 0 as common) of two F1 vector spaces.
        """
        if not isinstance(other, F1VS):
            raise TypeError("Direct sum is only defined between two F1VS instances.")
        
        # Combine elements, ensuring 0 is common
        combined_elements = self.elements | other.elements
        return F1VS(combined_elements)
    
    def quotient_space(self, subspace):
        """
        Compute the quotient space V/W where W is a subspace of V.
        """
        if not isinstance(subspace, F1VS):
            raise TypeError("Quotient space is only defined between F1VS instances.")
        if not subspace.elements.issubset(self.elements):
            raise ValueError("The subspace must be a subset of the original vector space.")
        
        # Define the equivalence classes
        quotient_elements = set()
        for v in self.elements:
            if v not in subspace.elements:
                quotient_elements.add(v)   
        return F1VS(quotient_elements)
