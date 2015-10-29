#include <cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include <tuple>
#include "gurobi_c++.h"

using namespace std;

int main(){//int argc,char** argv){
  int nbPOI= -1;
  int maxT= -1;
  //int dt= 1;
  
  cin>>nbPOI>> maxT;

  vector<double> reward (nbPOI, 0);
  vector<double> time (nbPOI, 0);
  vector< vector<double > > dist (nbPOI, vector<double>(nbPOI));
  for(int i =0; i<nbPOI; ++i){
    cin>> reward[i];
  }

  for(int i =0; i<nbPOI; ++i){
    cin>> time[i];
  }
  for(int i =0; i<nbPOI; ++i){
    for(int j =0; j<nbPOI; ++j){
      cin>> dist[i][j];
    }
  }
  try {
    GRBEnv env = GRBEnv();
    GRBModel* model = new GRBModel(env);

    vector< vector<GRBVar> > x(nbPOI, vector<GRBVar>(nbPOI));
    vector< GRBVar > ordre(nbPOI);

    for(int i =0; i<nbPOI; ++i){
      for(int j =0; j<nbPOI; ++j){
	x[i][j]=model->addVar(0.0, 1.0, 0.0, GRB_BINARY, "x_"+to_string(i)+to_string(j));
      }
    }
    for(int i =0; i<nbPOI; ++i){
      ordre[i]=model->addVar(0.0, GRB_INFINITY, 0.0, GRB_INTEGER, "o_"+to_string(i));
    }
    model->update();
    int constr_count=0;
    for(int i =0; i<nbPOI; ++i){
      for(int j =0; j<nbPOI; ++j){
	//sum of entering flow = sum entering flow
	GRBLinExpr expr1 = 0;
	GRBLinExpr expr2 = 0;
	for(int k=0; k<nbPOI; ++k){
	  expr1+= x[k][i];
	  expr2+=x[i][k];
	}
	model->addConstr(expr1-expr2, GRB_EQUAL, 0,"c_"+to_string(constr_count++));
	
	if(i==0) model->addConstr(expr1, GRB_EQUAL, 1,"c_"+to_string(constr_count++));
	else
	  model->addConstr(expr1, GRB_LESS_EQUAL, 1,"c_"+to_string(constr_count++));
      }
    }
   
    for(int i =0; i<nbPOI; ++i){
      for(int j =1; j<nbPOI; ++j){
	//order constraint
	GRBLinExpr expr = 0;
	expr+= ordre[i]-ordre[j]+1-nbPOI*(1-x[i][j]);
       	model->addConstr(expr, GRB_LESS_EQUAL, 0,"c_"+to_string(constr_count++));
      }
    }

    //Time constraint
    GRBLinExpr total_time = 0;
    for(int i =0; i<nbPOI; ++i){
      for(int j =0; j<nbPOI; ++j){
	total_time+= (dist[i][j]+time[j])*x[i][j];
      }
    }
    model->addConstr(total_time, GRB_LESS_EQUAL, maxT,"Time");

    //objective
    GRBLinExpr total_reward = 0;
    for(int i =0; i<nbPOI; ++i){
      for(int j =0; j<nbPOI; ++j){
	total_reward+= reward[j]*x[i][j];
      }
    }
    
    model->setObjective(total_reward, GRB_MAXIMIZE);
    model->update();
    model->optimize();
    int verbose=1;
    if(verbose>1){
    for(int i =0; i<nbPOI; ++i){
      for(int j =0; j<nbPOI; ++j){
	cout<<x[i][j].get(GRB_StringAttr_VarName) << ":"<<x[i][j].get(GRB_DoubleAttr_X)<<endl;
      }
    }
    for(int j =0; j<nbPOI; ++j){
      cout<<ordre[j].get(GRB_StringAttr_VarName) << ":"<<ordre[j].get(GRB_DoubleAttr_X)<<endl;
      }
    }
    //extract the path
    vector<int> path;
    bool found=0;
    int current=0;
    int final=0;
    bool finish=0;
    while(!finish){
      for(int j=0; j<(int)x[0].size();++j){

	if(x[current][j].get(GRB_DoubleAttr_X)>0){
	 	  //	      cout<<"on node"<<current<<" "<<j<<endl;
	  path.push_back(current);
	  //	  x[current][j]=0;
	  current=j;
	  if(current== final) finish=1;

	  found=1;
	  break;
	}
      }
      if(!found){
	cerr<<"Nothing interesting to do, going directly to final node"<<endl;
	path.push_back(current);
	current=final;
	finish=1;
      }
    }

    cout<<path.size()<<endl;
    for(uint i=0; i<path.size(); ++i)
      cout<<path[i]<<" ";
    cout<<endl;
	cout<<"The total reward is "<<model->get(GRB_DoubleAttr_ObjVal) << endl;
      } catch(...) {
	cout << "Exception during optimization" << endl;
      }
    }
