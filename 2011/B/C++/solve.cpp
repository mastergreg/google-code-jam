/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : solve.cpp

* Purpose :

* Creation Date : 11-09-2011

* Last Modified : Sun 11 Sep 2011 08:31:12 PM EEST

* Created By : Greg Liras <gregliras@gmail.com>

_._._._._._._._._._._._._._._._._._._._._.*/

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <list>
#include <vector>


using namespace std;



class mySuperClass
{
  private:
    list<string *> *contents;
    int counter;
    list < vector < int > * > *buildIndices(char c);
    bool letterIn;
  public:
    ~mySuperClass();
    mySuperClass(list<string *> *newContents,int newCounter);
    list<mySuperClass *> *next(char c);
    int getCounter();
    list<string *> *getString();
};



list<mySuperClass *> *buildStartWordListList(list<string *> *words);
list<mySuperClass *> *getNextLevel(list<mySuperClass *> *myWordList,char c);
string filterMaxString(list <string *> *dictionary, list <string *> *maxString);
list <string *> * findMax(list<mySuperClass *> *wordLists);


int main (int argc,char ** argv)
{
  int cases=0;
  cin >> cases;
  for(int i=1;i<=cases;i++)
  {
    int words=0;
    int letterSets=0;
    list<string *> *wordList = new list<string*>();
    list<string *> *letterList = new list<string*>();
    list<mySuperClass *> *wordLists;
    list<mySuperClass *> *currentWordLists;
    list<string *> *maxString;
    cout << "Case #" <<i<<":";
    cin >> words;
    cin >> letterSets;
    string *buff;
    for (int j=0;j<words;j++)
    {
      buff = new string();
      cin >> *buff;
      wordList->push_back(buff);
    }
    for (int j=0;j<letterSets;j++)
    {
      buff = new string();
      cin >> *buff;
      letterList->push_back(buff);
    }
    wordLists = buildStartWordListList(wordList);
    currentWordLists = wordLists;
    
    list<string *>::iterator letterString = letterList->begin();
    for(;letterString!=letterList->end();letterString++)
    {
      for (int j=0;j<26;j++)
      {
        currentWordLists = getNextLevel(currentWordLists,(**letterString)[j]);
      }
      maxString = findMax(currentWordLists);
      cout << " " <<filterMaxString(wordList,maxString);

    }
  }
}


string filterMaxString(list <string *> *dictionary, list <string *> *maxString)
{
  list<string *>::iterator finder = dictionary->begin();
  list<string *>::iterator sndFinder = maxString->begin();
  for(;finder!=dictionary->end();finder++)
  {
    for(;sndFinder!=maxString->end();sndFinder++)
    {
      if ((**finder)==(**sndFinder)) return **finder;
    }
  }
  return "NOTME!!!!";
}

list <string *> * findMax(list<mySuperClass *> *wordLists)
{
  int buf,max = -1;
  list<string *> * maxString;
  list<mySuperClass *>::iterator maxFound=wordLists->begin();
  for(;maxFound!=wordLists->end();maxFound++)
  {
    if((buf=(*maxFound)->getCounter())>max)
    {
      max=buf;
      maxString = (*maxFound)->getString();
    }
  }
  return maxString;
}

list<mySuperClass *> *getNextLevel(list<mySuperClass *> *myWordList,char c)
{
  list<mySuperClass *>::iterator current = myWordList->begin();
  list<mySuperClass *> *nextList = new list<mySuperClass *>();
  for(;current!=myWordList->end();current++)
  {
    list<mySuperClass *> *buff = (*current)->next(c);
    for (list<mySuperClass *>::iterator bf = buff->begin();bf!=buff->end();bf++)
    {
      nextList->push_back(*bf);
    }

  }
  return nextList;
}
list<mySuperClass *> *buildStartWordListList(list<string *> *words)
{
  list<string *>::iterator iter = words->begin();
  list<mySuperClass *> *rList = new list<mySuperClass *>();
  list<string *> *buff;
  for(int i = 1 ; i<=10;i++)
  {
    buff = new list<string *>();
    for(;iter!=words->end();iter++)
    {
      if ((*iter)->length()==i)
      {
        buff->push_back(*iter);
      }
    }
    rList->push_back(new mySuperClass(buff,0));
  }
  return rList;
}

list<string *> * mySuperClass::getString()
{
  return contents;
}

int mySuperClass::getCounter()
{
  return counter;
}
list < vector < int > *> *mySuperClass::buildIndices(char c)
{
  list<string *>::iterator word = contents->begin();
  list < vector < int > * > *indicesList = new list < vector < int >* >;
  vector < int > *buff;
  for (;word!=contents->end();word++)
  {
    buff = new vector<int>();
    for(int i=0;i<(**word).length();i++)
    {
      if (c== (**word)[i]) (*buff).push_back(c);
    }
    if (buff->size()>0) letterIn = true;
    indicesList->push_back(buff);
  }
  return indicesList;
}

mySuperClass::mySuperClass(list<string *> *newContents,int c)
{
  counter = c;
  contents = newContents;
  letterIn = false;
}

list<mySuperClass *> *mySuperClass::next(char c)
{
  list < vector < int > *> *allIndices = buildIndices(c);
  list<string*>::iterator word = contents->begin();
  list<string*>::iterator sndWord = contents->begin();
  list < vector < int > *>::iterator current = allIndices->begin();
  list < vector < int > *>::iterator sndCurrent = allIndices->begin();
  list <mySuperClass *> *rList = new list <mySuperClass *>();
  for (;word!=contents->end(),current!=allIndices->end();word++,current++)
  {
    list<string*> *buffer = new list<string*>();
    for(;sndWord!=contents->end() , sndCurrent!=allIndices->end();sndWord++,sndCurrent++)
    {
      if ((**current)==(**sndCurrent)) buffer->push_back((*sndWord));
    }
    if (((*current)->size()==0)&&letterIn)
    {
      rList->push_back(new mySuperClass(buffer,counter+1));
    }
    else
    {
      rList->push_back(new mySuperClass(buffer,counter));
    }
  }
  return rList;
}

