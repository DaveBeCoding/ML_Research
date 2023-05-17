### MLPClassifier



- The Accuracy for this problems model
* 22.77%

#### Model Reports
<details>
<summary>Click to expand</summary>

```markdown
The MLPClassifier is a multi-layer perceptron classifier that uses the backpropagation algorithm for training. It consists of multiple layers of nodes, each connected to the next layer, and can handle both classification and regression tasks.
```
To use the `MLPClassifier` model:
1. Initialize an instance of the model:
   ```python
   model = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', random_state=42)
</details>


#




### Sequential
- The Accuracy for this problems model
* 22.77%


#### Model Reports

| Epoch   | Train Loss | Train Accuracy | Val Loss | Val Accuracy |
|---------|------------|----------------|----------|--------------|
| 1/10    | nan        | 0.2568         | nan      | 0.2277       |
| 2/10    | nan        | 0.2568         | nan      | 0.2277       |
| 3/10    | nan        | 0.2568         | nan      | 0.2277       |
| 4/10    | nan        | 0.2568         | nan      | 0.2277       |
| 5/10    | nan        | 0.2568         | nan      | 0.2277       |
| 6/10    | nan        | 0.2568         | nan      | 0.2277       |
| 7/10    | nan        | 0.2568         | nan      | 0.2277       |
| 8/10    | nan        | 0.2568         | nan      | 0.2277       |
| 9/10    | nan        | 0.2568         | nan      | 0.2277       |
| 10/10   | nan        | 0.2568         | nan      | 0.2277       |
| Average | nan        | 0.2568         | nan      | 0.2277       |


<details>
<summary>Click to expand</summary>

```markdown
The Sequential model in Keras allows you to build neural network models in a sequential manner. It works by adding layers to the model one at a time in a linear stack.

To use the Sequential model:

1. Initialize an instance of the model:
   ```python
   model = Sequential()




