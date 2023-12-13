# Graph convert representation

This project includes a class `Graph` that contains the methods `dict_to_matrix` and `matrix_to_dict` that allows to convert the representation of graphs.

In other words:
- `dict_to_matrix` allows to convert the representation of type **Dict** into **`Matrix (list of lists)**.
- `matrix_to_dict` allows to convert the representation of type **Matrix (list of lists)** into **Dict**.

#### What is as Graph?
> According to [Wikipedia](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)), a graphs is _"a structure amounting to a set of objects in which some pairs of the objects are in some sense "related". The objects correspond to mathematical abstractions called vertices and each of the related pairs of vertices is called an edge."_. 

## How to Run
1. Clone this repository.
2. Run the following commands:
   - `python3 -m venv .venv`
   -  (Linux) `source .venv/bin/activate ` 
   
      (Windows) `.venv\Scripts\activate `
   - `pip install -r requirements.txt`
3. To run the tests cases, run this command: `python -m unittest tests.py`
4. 


---
_This is a resolution for the exercise of the Graphs Theory discipline, offered in the course Bachelor in Information Systems offered by IFNMG Januária._

**Issue details:**

> **A.** From the representation of a graph G as a dictionary, generate the Adjacency Matrix;
>
> **B.** From the representation of a graph G as an Adjacency Matrix, generate the dictionary representation;

