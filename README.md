# Algorithms and Data Structures (for Data Science)

This is a privately forked repository of the course I attended, the original repo can be found [HERE](https://github.com/rossanoventurini/adsds)!

* Teacher: [Rossano Venturini](http://pages.di.unipi.it/rossano)
* CFU: 9
* Period: Second semester
* Language: English
* Classroom: [here](https://classroom.google.com/u/0/c/Mzg4MzQ2ODk2MzQw) (code: dqwq6aj)
* Lectures schedule: Tuesday 14:15-16:00 (Aula Fib C), Thursday 14:15-16:00 (Aula Fib C), and Friday 9:00-10:45 (Aula Fib A1).
* Question time: After lectures or by appointment

## Goals and opportunities

The course introduces basic data structures and algorithmic techniques that allow students to solve computational problems on the most important data types, such as sequences, sets, trees, and graphs.

The lectures will be complemented by an intensive activity in laboratory.
Students will experiment with algorithms and data structures by writing their own implementations or by using third-party libraries.

The goal of the class is to enable students to design and implement efficient algorithms, choosing the most appropriate solutions in their future projects.

### Syllabus

- Introduction and basic definitions: algorithm, problem, instance.

- Computational complexity analysis of algorithms.

- Sorting: Mergesort, Quicksort and Heapsort.

- Searching: Binary Search, Binary Search Tree, Trie, and Hashing.

- Algorithms on Trees: representation and traversals.

- Algorithms on Graphs: representation, traversals, and most important problems.

- External memory model: sorting and searching.

## Exam

| Type | Date | Room | Note|
| ------------- | ------------- | ------------- | ----- |
| Lab | 19/07/2022 14:00 | Google Meet | Please send your solutions to me by 16/07/2022. **Important:**  Please Cut&Paste your solutions to this [Jupyter Notebook](Lab/Solutions_NAME_SURNAME.ipynb) and **send me just this file** with your name and surname on its filename. Please read the very important note below. |
| Lab | 01/09/2022 14:00 | Google Meet | Please send your solutions to me by 29/08/2022. **Important:**  Please Cut&Paste your solutions to this [Jupyter Notebook](Lab/Solutions_NAME_SURNAME.ipynb) and **send me just this file** with your name and surname on its filename. Please read the very important note below. |


**Very important!** You are allowed to discuss verbally solutions (e.g., a strategy to solve a problem) with other students, **BUT** you have to implement all the solutions by yourself. Thus, sharing implementations or implementing a solutions with others is strictly **forbidden**.

## References
*   Introduction to Algorithms,  3rd Edition, Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, The MIT Press, 2009 ([Amazon](http://www.amazon.com/Introduction-Algorithms-3rd-Thomas-Cormen/dp/0262033844/ref=sr_1_1?s=books&ie=UTF8&qid=1443160441&sr=1-1&keywords=introduction+to+algorithms)) [CCLR]
*   Algorithms, 4th Edition, Robert Sedgewick, Kevin Wayne, Addison-Wesley Professional, 2011 ([Amazon](http://www.amazon.com/Algorithms-4th-Edition-Robert-Sedgewick/dp/032157351X/ref=pd_sim_14_2?ie=UTF8&refRID=1A2NFN935EST0ZQARB6H&dpID=51UDgHU9z9L&dpSrc=sims&preST=_AC_UL160_SR130%2C160_)) [RS]
*   Algorithms, Sanjoy Dasgupta, Christos Papadimitriou, Umesh Vazirani, McGraw-Hill, 2006\. ([Amazon](http://www.amazon.com/Algorithms-Sanjoy-Dasgupta/dp/0073523402)) [DPZ]

## Lectures
| Date | Lecture | References | Material |
| ------------- | ------------- | ------------- | ------------- |
| 15/02/2022 | Introduction to analysis of algorithms.| CCLR Sect. 2.1 | [Notes next 3 lectures](Notes/Analysis22.pdf)|
| 17/02/2022 | Insertion Sort: Correctness and analysis.| CCLR Sect. 2.2 | [VisuAlgo Sorting](https://visualgo.net/en/sorting) |
| 18/02/2022 | Selection Sort: Correctness and analysis.|  | [Selection Sort vs Insertion Sort ](Notes/L01_Insertion_Sort_vs_Selection_Sort.ipynb) and [VisuAlgo Sorting](https://visualgo.net/en/sorting)|
| 22/02/2022 | Divide and Conquer. Merge Sort. | CCLR Sect. 2.3  | [VisuAlgo Sorting](https://visualgo.net/en/sorting) and  [Notes next 3 lectures](Notes/Mergesort22.pdf) |
| 24/02/2022 | Divide and Conquer. Merge Sort. (contd)| CCLR Sect. 2.3  | [VisuAlgo Sorting](https://visualgo.net/en/sorting) |
| 25/02/2022 | **Laboratory Lecture 01**: Basics sorting | | [Jupyter Notebook](Lab/Lecture_01/L01_Basic_Sorting_no_sols.ipynb) **Mandatory exercises** |
| 01/03/2022 | Exercises with recurrences. Binary search. | CCLR Sect 3.1 | |
| 03/03/2022 | QuickSort. Best and worst cases. No average time analysis. | CCLR Sects 7.1, 7.2, and 7.3. | [VisuAlgo Sorting](https://visualgo.net/en/sorting) and [Notes next 2 lectures](Notes/Quicksort22.pdf) |
| 04/03/2022 | **Laboratory Lecture 02**: MergeSort and QuickSort. | | [Jupyter Notebook](Lab/Lecture_02/L02_Sorting_no_sols.ipynb) **Mandatory exercises** | 
| 08/03/2022 | QuickSort. Best and worst cases. No average time analysis.  Asymptotic notation.| CCLR Sects 7.1, 7.2, and 7.3. |  |
| 10/03/2022 | Lower Bound for sorting in the comparison model. | CCLR Sect. 8.1 |[Notes](Notes/Lowerbound22.pdf) |
| 11/03/2022 | **Laboratory Lecture 03**: Applications of sorting (I). | | [Jupyter Notebook](Lab/Lecture_03/L03_Sorting_Applications_Greedy_Algorithms_no_sols.ipynb) **Mandatory exercises** |  
| 15/03/2022 | Sorting in linear time: Counting Sort. | CCLR Sect. 8.2 | [VisuAlgo Sorting](https://visualgo.net/en/sorting). [Notes next 2 lectures](Notes/LinearTimeSorting22.pdf)| 
| 17/03/2022 | Sorting in linear time: Radix Sort. | CCLR Sect. 8.3.| [VisuAlgo Sorting](https://visualgo.net/en/sorting) | 
| 18/03/2022 | Dictionary problem with Hashing.| CCLR Sect. 11.1, 11.2, and 11.4 (no analysis) | [Notes next 2 lectures](Notes/Hashing22.pdf) | 
| 22/03/2022 | Dictionary problem with Hashing. | CCLR Sect. 11.1, 11.2, and 11.4 (no analysis) | |
| 24/03/2022 | Python best practices. | | |
| 25/03/2022 | **Laboratory**: Hashing. Python best practices. | | [Jupyter Notebook](Lab/Lecture_04/L04_Hashing_no_sols.ipynb) **Mandatory exercises** |
| 29/03/2022 | Python best practices. | | |
| 31/03/2022 | Python best practices. | | |
| 01/04/2022 | **Laboratory**: Hashing: Applications.  | | [Jupyter Notebook](Lab/Lecture_05/L05_Hashing_Applications_no_sols.ipynb) **Mandatory exercises** |
| 04/04/2022 | QuickSelect. Priority queues: Heap. | CCLR Sect. 9.1, 9.2 and CCLR Ch. 6 | [Notes next 3 lectures](Notes/Heap.pdf) |
| 07/04/2022 | Priority queues: Heap. | CCLR Ch. 6 | [VisuAlgo Heap](https://visualgo.net/en/heap?slide=1) | 
| 08/04/2022 | **Laboratory**: Applications of sorting (II). | | [Jupyter Notebook](Lab/Lecture_06/L06_Sorting_Applications_II_no_sols.ipynb) **Mandatory exercises** |
| 12/04/2022 | Priority queues: Heap. | CCLR Ch. 6 | [VisuAlgo Heap](https://visualgo.net/en/heap?slide=1) |
| 14/04/2022 | Binary Search tree. | CCLR Sect. 12.1, 12.2, and 12.3  | [Visualgo BST](https://visualgo.net/en/bst) | [Notes for next two lectures](Notes/Bst.pdf) |
| 21/04/2022 | Binary Search tree. | CCLR Sect. 12.1, 12.2, and 12.3  | [Visualgo BST](https://visualgo.net/en/bst) |  | 
| 22/04/2022 | **Laboratory**: Binary Search Tree.  | | [Jupyter Notebook](Lab/Lecture_07/L07_Binary_Search_Tree_no_sols.ipynb) **Mandatory exercises** |
| 26/04/2022 | Exercises: Visits of a tree. |  | [Notes next 2 lectures](Notes/Trees.pdf) | | 
| 28/04/2022 | Exercises: Visits of a tree. |  | | | 
| 03/05/2022 | Graphs: representations and BFS. |CCLR Sect. 22.1 and 22.2 (no proofs) | [Notes next 2 lectures](Notes/Graphs.pdf) | 
| 05/05/2022 | Graphs: DFS. |CCLR Sect. 22.3 (no proofs) | [Graph representations](https://visualgo.net/en/graphds) and [BFS/DFS](https://visualgo.net/en/dfsbfs) |
| 06/05/2022 | **Laboratory**: Questions| |
| 10/05/2022 | Exercises | [Notes](Notes/Exam20210610_sol.pdf) |
| 12/05/2022 | Exercises | [Notes](Notes/Exam20210723_sol.pdf)|
| 13/05/2022 | **Laboratory**: Graphs.  | | [Jupyter Notebook](Lab/Lecture_08/L08_Graphs_with_NetworkX_no_sols.ipynb) **Mandatory exercises** |

