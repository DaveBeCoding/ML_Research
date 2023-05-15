#include <iostream>
#include <vector>

class Operation {
public:
    std::vector<Operation*> input_nodes;
    std::vector<Operation*> output_nodes;

    Operation(std::vector<Operation*> input_nodes = {}) {
        this->input_nodes = input_nodes;
        
        for(auto node : input_nodes){
            node->output_nodes.push_back(this);
        }
    }
};


int main(){


    std::cout << "pass" << std::endl;

return 0;
}
