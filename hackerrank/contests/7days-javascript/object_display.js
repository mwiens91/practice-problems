function displayInformation() {
  for (book in library) {
    if (library[book].readingStatus === true) {
      console.log("Already read '"
                  + library[book].title
                  + "' by "
                  + library[book].author
                  +".")
    } else {
      console.log("You still need to read '"
                  + library[book].title
                  + "' by "
                  + library[book].author
                  +".")
    }
  }
}

// tail starts here
var library = [
  {
     title: 'Bill Gates',
     author: 'The Road Ahead',
     readingStatus: true
  },
  {
     title: 'Steve Jobs',
     author: 'Walter Isaacson',
     readingStatus: true
  },
  {
     title: 'Mockingjay: The Final Book of The Hunger Games',
     author: 'Suzanne Collins',
     readingStatus: false
  }
];

displayInformation();
