import re
import pandas as pd
def decode_ebcdic_columns(df, columns_to_decode=None):
    """Decode EBCDIC encoded columns in DataFrame"""
    
    if columns_to_decode is None:
        # Auto-detect binary columns
        columns_to_decode = []
        for col in df.columns:
            if df[col].dtype == 'object':
                # Check if column contains bytes
                sample = df[col].dropna().iloc[0] if len(df[col].dropna()) > 0 else None
                if isinstance(sample, bytes):
                    columns_to_decode.append(col)
    
    for col in columns_to_decode:
        try:
            # Try different EBCDIC code pages
            df[col] = df[col].apply(lambda x: 
                x.decode('cp500').rstrip('@').rstrip() if isinstance(x, bytes) else x
            )
        except:
            try:
                # Alternative EBCDIC encoding
                df[col] = df[col].apply(lambda x: 
                    x.decode('cp037').rstrip('@').rstrip() if isinstance(x, bytes) else x
                )
            except:
                # Keep original if decoding fails
                pass
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].apply(lambda x: re.compile(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F-\x9F]').sub('', str(x).replace('→', '->')) if pd.notna(x) else "")
    return df