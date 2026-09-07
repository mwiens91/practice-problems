// @leet start
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function (beginWord, endWord, wordList) {
  const WORD_LENGTH = beginWord.length;
  wordList.push(beginWord);

  const adjLists = new Map();

  for (let i = 0; i < wordList.length; i++) {
    for (let j = i + 1; j < wordList.length; j++) {
      let diffs = 0;

      for (let k = 0; k < WORD_LENGTH; k++) {
        if (wordList[i][k] !== wordList[j][k]) {
          diffs++;

          if (diffs > 1) {
            break;
          }
        }
      }

      // If diffs <= 1 there's an edge between the ith and jth word
      if (diffs <= 1) {
        if (!adjLists.has(wordList[i])) {
          adjLists.set(wordList[i], []);
        }

        if (!adjLists.has(wordList[j])) {
          adjLists.set(wordList[j], []);
        }

        adjLists.get(wordList[i]).push(wordList[j]);
        adjLists.get(wordList[j]).push(wordList[i]);
      }
    }
  }

  if (!adjLists.has(beginWord)) {
    return 0;
  }

  // BFS
  let currLevel = [beginWord];
  let seqLength = 1;
  const seen = new Set([beginWord]);

  while (currLevel.length) {
    const nextLevel = [];

    for (const curr of currLevel) {
      for (const adj of adjLists.get(curr)) {
        if (adj === endWord) {
          return seqLength + 1;
        }

        if (!seen.has(adj)) {
          seen.add(adj);
          nextLevel.push(adj);
        }
      }
    }

    currLevel = nextLevel;
    seqLength++;
  }

  return 0;
};
// @leet end
