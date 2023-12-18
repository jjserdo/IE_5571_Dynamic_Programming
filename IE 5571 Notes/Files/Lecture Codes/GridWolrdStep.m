function S_new=GridWolrdStep(S_old,Action)
%takes old position and action, and generates new position.
%system takes place on a 7x10 grid.
%all episodes start at row 4, column 1, and ends at row 4, column 8.
%we will work with 3 coordinate systems 1)row and column, 2) cartesian
%coordinate, 3) linear coordinate
%S_old, and S_new are in linear coordinate.

%
GridH=7;
GridW=10;
%Wind vector
Wind=[0 0 0 1 1 1 2 2 1 0];

[row,col]=ind2sub([GridH,GridW],S_old);
y_old=GridH-row;
x_old=col-1;

x=max(min(x_old+Action(1),GridW-1),0);
y=max(min(y_old+Action(2)+Wind(x+1),GridH-1),0);


row=GridH-y;
col=x+1;
S_new=sub2ind([GridH,GridW],row,col);



