import unittest

from covertutils.orchestration import StegoOrchestrator

from covertutils.datamanipulation import StegoInjector




class Test_StegoOrchestrator( unittest.TestCase ) :


	configuration = [( ('simple:X','simple:X'),('!H','!H'), '_data_+1' )]

	stego_conf = """

X:_data_:
Y:_data_:

simple='''4142XXXXXXXXYYYYYYYY4344'''
control='''4142XXXXXXXXYYYYYYYY4344'''

	"""

	def setUp(self) :

		self.orch1 = StegoOrchestrator( "a", self.stego_conf )
		self.orch2 = StegoOrchestrator( "a", self.stego_conf, reverse = True )


	def test_functionality( self ) :

		data = "0"*5

		chunks = self.orch1.readyMessage( data, 'simple' )
		print chunks[0].encode('hex')

		for chunk in chunks :
			stream, message = self.orch2.depositChunk( chunk )

			print stream ,message
		self.failUnless( data == message )
