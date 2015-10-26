# Makefile Generique
 
EXT = cpp
CXX = g++ -g
EXEC = LP
 
DEBUG = 
CXXFLAGS =-O3 -Wall -W -pedantic  -I/opt/gurobi602/linux64/include/ -std=c++11 -lpthread -lm -L/opt/gurobi602/linux64/lib/ -lgurobi_c++ -lgurobi60
LDFLAGS = -I/opt/gurobi602/linux64/include/ -std=c++11 -lpthread -lm -L/opt/gurobi602/linux64/lib/ -lgurobi_c++ -lgurobi60 -O2
 
 
OBJDIR = obj
SRC = $(wildcard *.$(EXT))
OBJ = $(SRC:.$(EXT)=.o)
OBJ := $(addprefix $(OBJDIR)/, $(OBJ))
 
all: $(EXEC)
 
$(EXEC): $(OBJ)
	@$(CXX) -o $@ $^ $(LDFLAGS) $(DEBUG)
 
$(OBJDIR)/%.o: %.$(EXT)
	@$(CXX) -o $@ -c $< $(CXXFLAGS)$(DEBUG)
 
clean:
	@rm -rf $(OBJDIR)/*.o
	@rm -f $(EXEC)

