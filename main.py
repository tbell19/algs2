class Node:
    def __init__(self,parent,name,courseNumber) -> None:
        #create a new node
        self.edges = []
        self.name = name
        self.courseNumber = courseNumber
        self.visited = False
        self.parent = parent
        pass
    
    def addEdge(self,courseNumber):
        for node in self.parent.graph:
            if node.courseNumber == courseNumber:
                self.edges.append(node)
                break
        else:
            raise Exception("Unable to find node \""+courseNumber+"\", please define node before adding as edge to another node.")
        return self



class Graph:
    def __init__(self):
        self.graph = []
        pass

    def addNode(self,name,courseNumber):
        newNode = Node(self,name,courseNumber)
        self.graph.append(newNode)
        return newNode



def main():
    print("starting up")
    courseGraph = Graph()
    courseGraph.addNode("Programming Principles I","CS 1411")
    courseGraph.addNode("Calculus I wiht Applications","MATH 1451")
    courseGraph.addNode("Essentials of College Rhetoric","ENGL 1301")
    courseGraph.addNode("Programming Principles II","CS 1412").addEdge("CS 1411")
    courseGraph.addNode("Calculus II with Applications","MATH 1452").addEdge("MATH 1451")
    courseGraph.addNode("Principles of Physics I","PHYS 1408").addEdge("MATH 1451")
    courseGraph.addNode("Advanced College Rhetoric","ENGL 1302").addEdge("ENGL 1301")
    courseGraph.addNode("Data Structures","CS 2413").addEdge("CS 1412")
    courseGraph.addNode("Discrete Computational Structures","CS 1382").addEdge("CS 1411")
    courseGraph.addNode("Modern Digital System Design","ECE 2372").addEdge("MATH 1451")
    courseGraph.addNode("Calculus III with Applications","MATH 2450").addEdge("MATH 1452")
    courseGraph.addNode("Principles of Physics II","PHYS 2401").addEdge("PHYS 1408")
    courseGraph.addNode("Computer Organization and Assembly Language Programming","CS 2350").addEdge("CS 1412").addEdge("ECE 2372")
    courseGraph.addNode("Object-Oriented Programming","CS 2365").addEdge("CS 2413")
    courseGraph.addNode("Engineering Ethics and Its Impact on Society","ENGR 2392")
    courseGraph.addNode("American Government","POLS 1301")
    courseGraph.addNode("Linear Algebra","MATH 2360").addEdge("MATH 1452")
    courseGraph.addNode("Introduction to Technical Writing","ENGL 2311").addEdge("ENGL 1301").addEdge("ENGL 1302")
    courseGraph.addNode("Concepts of Programming Languages","CS 3361").addEdge("CS 2413")
    courseGraph.addNode("Design and Analysis of Algorithms","CS 3364").addEdge("CS 2413").addEdge("CS 1382").addEdge("MATH 2360")
    courseGraph.addNode("Mathematical Statistics for Engineers and Scientists","MATH 3342").addEdge("MATH 2450")
    courseGraph.addNode("Texas Politics and Topics","POLS 2306")
    courseGraph.addNode("Software Engineering I","CS 3365").addEdge("CS 2365").addEdge("CS 2413").addEdge("MATH 3342")
    courseGraph.addNode("Computer Architecture","CS 3375").addEdge("CS 2350")
    courseGraph.addNode("Theory of Automata","CS 3383").addEdge("CS 1382")
    courseGraph.addNode("Software Engineering II","CS 4365").addEdge("CS 3365")
    courseGraph.addNode("Operating Systems","CS 4352").addEdge("CS 3364").addEdge("CS 3375")
    courseGraph.addNode("Concepts of Database Systems","CS 4354").addEdge("CS 3364")
    courseGraph.addNode("Senior Capstone Project","CS 4366").addEdge("CS 4365")
    print("test")

if __name__ == "__main__":
    main()