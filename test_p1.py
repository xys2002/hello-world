from p1 import hello_world

def test_p1(capsys):
     hello_world()
     out,_=capsys.readouterr()
     assert out=="Hello World!\n"