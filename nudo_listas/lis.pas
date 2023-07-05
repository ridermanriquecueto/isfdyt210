program ListaEnlazada;

type
  PNodo = ^Nodo;
  Nodo = record
    dato: integer;
    siguiente: PNodo;
  end;

var
  cabeza, actual, nuevoNodo: PNodo;
  valor: integer;
  opcion: char;

begin
  cabeza := nil;
  repeat
    writeln('Ingrese el valor:');
    readln(valor);

    New(nuevoNodo);
    nuevoNodo^.dato := valor;
    nuevoNodo^.siguiente := nil;

    if cabeza = nil then
    begin
      cabeza := nuevoNodo;
      actual := cabeza;
    end
    else
    begin
      actual^.siguiente := nuevoNodo;
      actual := actual^.siguiente;
    end;

    writeln('Desea agregar otro elemento? (S/N)');
    readln(opcion);
  until (opcion = 'N') or (opcion = 'n');

  writeln('La lista enlazada ingresada es:');
  actual := cabeza;
  while actual <> nil do
  begin
    writeln(actual^.dato);
    actual := actual^.siguiente;
  end;
end.
