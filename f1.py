class F1VS:
    def __init__(self, elements):
        """
        Initialize the F1 vector space with a set of elements.
        Ensure that the base element 0 is included.
        """
        self.elements = set(elements)
        self.elements.add(0)  # Ensure 0 is included as the base element

    def __repr__(self):
        return f"{self.elements}"

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
    
    def dimn(vector_space):
        if isinstance(vector_space, F1VS):
            return len(vector_space.elements) - 1
        else:
            raise TypeError("Expected an instance of F1VS")

class F1Map:
    def __init__(self, V1, V2, mapping):
        """Define a function f: V1 → V2 that satisfies:
        - f(0) = 0
        - Injectivity on nonzero elements: No two elements map to the same nonzero."""
        if not isinstance(V1, F1VS) or not isinstance(V2, F1VS):
            raise TypeError("Both domain and codomain must be instances of F1VS.")
        
        self.V1 = V1
        self.V2 = V2
        self.mapping = {}

        # Ensure 0 maps to 0
        if mapping.get(0, 0) != 0:
            raise ValueError("The function must map 0 to 0.")

        # Track used nonzero elements in V2 to enforce injectivity
        used_values = set()
        
        for v1, v2 in mapping.items():
            if v1 != 0:  # Nonzero element
                if v2 != 0:
                    if v2 in used_values:
                        raise ValueError("Injectivity violated: Two elements of V1 map to the same nonzero in V2.")
                    if v2 not in V2.elements:
                        raise ValueError(f"Element {v2} is not in V2.")
                    used_values.add(v2)
                elif v2 not in V2.elements:
                    raise ValueError(f"Element {v2} is not in V2.")
            
            self.mapping[v1] = v2  # Store the valid mapping

    def __repr__(self):
        return f"F1Map({self.mapping})"

    def apply(self, element):
        """Apply the function to an element of V1."""
        if element not in self.V1.elements:
            raise ValueError(f"Element {element} is not in V1.")
        return self.mapping.get(element, 0)  # Default to 0 if not explicitly mapped
    
    def kernel(self):
        """Compute the kernel of the map (elements in V1 that map to 0 in V2)."""
        kernel_elements = {x for x in self.V1.elements if self.mapping.get(x, 0) == 0}
        return F1VS(kernel_elements)
    
    def image(self):
        """Compute the image of the map (elements in V2 that are mapped to)."""
        image_elements = {self.mapping.get(x, 0) for x in self.V1.elements}
        return F1VS(image_elements)

    def is_isomorphic(self):
        """Check if the function is an isomorphism (bijective)."""
        # Check injectivity (kernel must be {0})
        if self.kernel().elements != {0}:
            return False

        # Check surjectivity (image must be equal to V2)
        if self.image().elements != self.V2.elements:
         return False

        return True
