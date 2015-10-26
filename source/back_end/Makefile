all:
	g++ -g LP.cpp -O3 -Wall -W -pedantic  -I/opt/gurobi602/linux64/include/ -std=c++11 -lpthread -lm -L/opt/gurobi602/linux64/lib/ -lgurobi_c++ -lgurobi60 -I/opt/gurobi602/linux64/include/ -std=c++11 -lpthread -lm -L/opt/gurobi602/linux64/lib/ -lgurobi_c++ -lgurobi60 -O2 

clean:
	@rm -rf $(OBJDIR)/*.o
	@rm -f $(EXEC)

