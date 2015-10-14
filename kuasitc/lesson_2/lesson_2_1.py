import sys

for i in range( 1, 10):
	for j in range( 1, 10):
		sys.stdout.write( '%sx%s = %s\t' % ( i, j, i * j ) )
	sys.stdout.write( '\n')