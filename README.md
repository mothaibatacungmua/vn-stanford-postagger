# vn-stanford-postagger

This is a part-of-speech tagging tool for vietnamese text. The development of this tool depends on  the open source implementation of [Stanford Log-linear Part-Of-Speech Tagger](http://nlp.stanford.edu/software/tagger.shtml).

We use [JVnTextPro](http://jvntextpro.sourceforge.net/) for text preprocessing task including sentence segmentation, sentence tokenization and word segmentation.

##### Experiments<br/>
The models are trained and tested on the part-of-speech tagged section of the Vietnamese treebank (~27000 sentences). The treebank's sentences are manually segmented and tagged.<br/>
Evaluation of the trained models is performed classically using 10-fold cross-validation, where the corpus is randomly split into 10 parts which are each used for testing a model built using data from the 9 others.

| Fold          | Total tags    | Unknown words  |
| ------------- |:-------------:| :-------------:|
| Fold 1        | 94.37%        | 78.12%         |
| **Fold 2**    | **94.52%**    | 78.30%         |
| Fold 3        | 94.47%        | 79.41%         |
| Fold 4        | 94.43%        | **81.12%**     |
| Fold 5        | 94.29%        | 78.12%         |
| Fold 6        | 94.24%        | 80.24%         |
| Fold 7        | 94.29%        | 80.86%         |
| Fold 8        | 94.39%        | 78.77%         |
| Fold 9        | 94.34%        | 79.00%         |
| Fold 10       | 94.22%        | 79.78%         |
| **Avg.**      | **94.36%**    | **79.37%**     |

![alt text](https://github.com/tuantq57/vn-stanford-postagger/blob/master/result/POSTagging.png "Total result")

##### References<br/>
1. [Enriching the Knowledge Sources Used in a Maximum Entropy Part-of-Speech Tagger](http://nlp.stanford.edu/~manning/papers/emnlp2000.pdf) <br/>
2. [Feature-Rich Part-of-Speech Tagging with a Cyclic Dependency Network](http://nlp.stanford.edu/pubs/tagging.pdf) <br/>
3. [JVnTagger](http://www.jaist.ac.jp/~bao/VLSP-text/Mar2009/SP83-Baocaokythuat2009thang3.pdf) <br/>
4. [Manual for JVnTextPro](http://jvntextpro.sourceforge.net/v2.0/JVnTextPro_Manual.pdf) <br/>
5. [An empirical study of maximum entropy approach for part-of-speech tagging of Vietnamese texts](https://hal.archives-ouvertes.fr/inria-00526139/)