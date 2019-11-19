node = ["X" "X" "X" "X" "C" "B" "B" "A" "L" "L" "H" "H" "D" "J" "I" "G" "K"];  
tonode = ["C" "E" "B" "A" "L" "H" "D" "D" "J" "I" "G" "F" "F" "I" "K" "Y" "Y"];
weights = [3 4 2 7 2 5 4 4 1 4 2 3 1 6 4 2 5];
G = graph(node,tonode,weights);
p = plot(G,'EdgeLabel',G.Edges.Weight)
[P,d] = shortestpath(G,"X","Y")
highlight(p,P,'EdgeColor','r')
