
"""
Das "with" Keyword beinhaltet dieselben Funktionen und ist eine Zeile kürzer.
Das Schließen wird hier automatisch übernommen.
Fehler (etwa bei dem Versuch ein Dokument mit "x" zu erstellen das bereits existiert)
werden gehandlet und führen nicht zu einer Beendigung der Ausführung.
"""
def read_projects():
  with open("k21-3-projects.txt") as file:
    print(file.read())
  return
    
'''
Wir können dem FileStream noch zusätzliche Argumente mitgeben:

  r => Read => Datei lesen (Default).
  x => Create => Datei erstellen. Fehler falls Datei vorhanden.
  w => Write => Schreibt in angegebene Datei. Überschreibt existierende Datei, falls vorhanden.
  a => Append => Erweitert die Datei am Ende des Dokuments.

Ein durch 'r' geöffnetes Dokument, kann durch die read() function ausgelesen werden.

Ein mit 'r' 'w' 'a' geöffnetes Dokument kann durch write(<string>) beschrieben werden.

Das zweite Argument des Filestreams kann 't' für text oder 'b' binary darstellen. Hierbei ist 't' der default Wert.

Um ein Dokument zu löschen kann das 'os'Modul importiert werden. Darin ist die remove() Funktion, mit der wir
Dateien in dem Filesystem löschen können.
'''

def read_and_return(doc_path: str) -> str:
  f = open(doc_path, 'r')
  res = f.read()
  f.close()
  return res

def write_in_mode(doc_path: str, data: str, file_mode :str ='w'):
  f = open(doc_path, file_mode)
  f.write(data)
  f.close()
  
def delete_doc(doc_path: str):
  import os
  os.remove(doc_path)
  
  
"""
Häufig ist sowohl Lese- als auch Schreibberechtigung bei dem Bearbeiten von Dateien erwünscht.
Um das gewünschte Verhalten zu erreichen sind folgende Argument"kombinationen" möglich:
  r+   Datei Lesen und überschreibend erweitern.
    -> Fehlerrückgabe falls Datei nicht vorhanden.  
    -> Der "Cursor" wird an den Anfang des Dokuments platziert.
  w+   Datei überschreiben und Lesen.
    -> Erstellt neue Datei falls nicht vorhanden.
    -> Überschreibt neue Datei falls vorhanden.
  a+   Datei erweitern und Lesen.
    -> Erstellt neue Datei falls nicht vorhanden.
    -> Der "Cursor" wird an das Ende des Dokuments platziert.
"""



def main():
  mitarbeiter_a = {
    "name": "Herbert",
    "age": 42
  }
  # print(read_and_return("k21-3-projects.txt"))
  # write_in_mode("example.txt", mitarbeiter_a.__str__(), 'a')
  delete_doc("example.txt")
  
if __name__ == '__main__':
  main()