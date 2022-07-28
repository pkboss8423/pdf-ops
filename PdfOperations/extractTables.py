import os
import tabula
from PdfOperations.deletePages import create_array
from Utils.createFolder import  create_tables_folder

def extract_tables(st,file,pages):
    x = create_tables_folder()
    z = create_array(pages)
    z.sort()
    c=1 
    if len(z) != 0:
        for i in z:
            dfs = tabula.read_pdf(file, pages=i+1)
            for i in range(len(dfs)):
                path = os.path.join(x, "Table"+f"{c}"+".csv")
                dfs[i].to_csv(path, index=False)
                c += 1
    else:
        dfs = tabula.read_pdf(file, pages='all')
        for i in range(len(dfs)):
            path = os.path.join(x, "Table"+f"{c}"+".csv")
            dfs[i].to_csv(path, index=False)
            c += 1
    st.write(f"Process Completed. Path={x}")    
            
