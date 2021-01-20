import blendfile
import os
import sys
def get_id_name(block):
    name = block[b'id', b'name'].decode()
    return name[2:]

for fname in sys.argv[1:]: #"/Users/hezishahmoon/Downloads/Super_Blender_Galaxy/levels/level_1.blend"
    fPath,fTitle = os.path.split(fname)
    bf = blendfile.open_blend(fname)
    texts = bf.find_blocks_from_code(b'TX')
    for t in texts:
        i = s = bf.blocks.index(t) + 1
        print("Saving File: "+get_id_name(t))
        with open(fname+"."+get_id_name(t)+".py",'w') as f:
            while bf.blocks[i].dna_type_name == 'TextLine':
                # Get the block
                block = bf.blocks[i]
                # Get the length
                length = block[b'len']
                # Get the line data pointer (a block)
                line = block.get_pointer( b'line')

                # Search for the line block position
                bf.handle.seek( line.file_offset, 0 )

                # Get the value
                line_content = blendfile.DNA_IO.read_string( bf.handle, length )

                #print( i - s )
                #print( bf.blocks[i][b'len'] )
                f.write( line_content+"\n" )


                #print( bf.blocks[i].user_data )
                #print(f"line {i - s} chars {bf.blocks[i][b'len']}")
                i += 1
    bf.close()