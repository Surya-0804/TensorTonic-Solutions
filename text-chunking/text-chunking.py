def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    final_chunks=[]
    step=chunk_size-overlap
    for i in range(0,len(tokens),step):
        chunk = tokens[i:i+chunk_size]
        final_chunks.append(chunk)
        if i + chunk_size >= len(tokens):
            break
    return final_chunks