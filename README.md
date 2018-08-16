# Chimera-Scripts

## Adding Hydrogens

When saving a molecule from the Protein Data Bank (PDB), if the structure is the result of a x-ray crystallography experiment, the structure will not include the hydrogens. This is because x-ray crystallography measures the &quot;electron density&quot; of a molecule, and hydrogen (the smallest atom) is invisible to this technique. This can also lead to a host of ambiguities, including difficult assigning between oxygen and nitrogen, as these two atoms are similar in regards to electron density.

This exclusion of hydrogen is sad, however; many chemistry structure visualization tools can automatically add this atom back in. UCFS Chimera is one such tool, and since its inclusion of the popular programming language, Python, Chimera has opened the door to large scale, automated structure editing.

By saving and running the code below in Chimera, the program will add hydrogens to all structures in the same directory as the python file, and save these as new files.


1. Berman, H. M.; Westbrook, J.; Feng, Z.; Gilliland, G.; Bhat, T. N.; Weissig, H.; Shindyalov, I. N.; Bourne, P. E., The Protein Data Bank. _Nucleic Acids Research_ **2000,** _28_ (1), 235-242.

2. Smyth, M. S.; Martin, J. H. J., x Ray crystallography. _Molecular Pathology_ **2000,** _53_ (1), 8-14.

3. Fan, H.; Mark, A. E., Refinement of homology-based protein structures by molecular dynamics simulation techniques. _Protein Science : A Publication of the Protein Society_ **2004,** _13_ (1), 211-220.

4. Pettersen, E. F.; Goddard, T. D.; Huang, C. C.; Couch, G. S.; Greenblatt, D. M.; Meng, E. C.; Ferrin, T. E., UCSF Chimera--a visualization system for exploratory research and analysis. _Journal of computational chemistry_ **2004,** _25_ (13), 1605.
