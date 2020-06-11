def read_csv(filename):
    '''Read a csv into a list of dicts, i.e.,
       [{"col1": col1_row1, "col2": col2_row1, ... }, {"col1": col1_row2, ...},
        ...]
    '''

    # Quoted scanout results does not appear to have arbitrary newlines.

    with open(filename, 'r') as i:
        columns = [u.strip('"') for u in i.readline().strip().split(',')]
        lines = [{v: u.strip('"') for v, u in zip(columns, line.strip().split(','))} for line in i]

    return lines, columns
