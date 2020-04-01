const $playButton = document.querySelector('#play-button')
const $pauseButton = document.querySelector('#pause-button')
const $stepBackwardButton = document.querySelector('#step-backward-button')
const $stepForwardButton = document.querySelector('#step-forward-button')
const $audio = document.querySelector('#audio')
const $playingSong = document.querySelector('#playing-song')
const $playingArtist = document.querySelector('#playing-artist')
const $playingAlbum = document.querySelector('#playing-album')
const $playingCover = document.querySelector('#playing-cover')
const $songAnchors = document.querySelectorAll('.song')
let playing = false

function play() {
  $playButton.classList.add('is-hidden')
  $pauseButton.classList.remove('is-hidden')
  $audio.play()
  playing = true
}

function pause() {
  $playButton.classList.remove('is-hidden')
  $pauseButton.classList.add('is-hidden')
  $audio.pause()
  playing = false
}

function stop() {
  pause()
  $audio.currentTime = 0
}

function stepBackward() {
  $audio.currentTime = 0
}

function stepForward() {
  stop()
}

function togglePlaying() {
  if (playing) {
    pause()
  } else {
    play()
  }
}

function changeSong(e) {
  e.preventDefault()
  let currentNode = e.target

  while (currentNode.nodeName !== 'ARTICLE') {
    currentNode = currentNode.parentElement
  }
  const songName = currentNode.querySelector('.song-name').innerHTML
  const artistName = currentNode.querySelector('.artist-name').innerHTML
  const albumName = currentNode.querySelector('.album-name').innerHTML
  const coverSrc = currentNode.querySelector('.cover').src

  $playingSong.innerHTML = songName
  $playingArtist.innerHTML = artistName
  $playingAlbum.innerHTML = albumName
  $playingCover.src = coverSrc

  $audio.src = currentNode.dataset.url
  play()
}

$audio.addEventListener('ended', () => {
  stop()
})

$audio.addEventListener('play', e => {
  play()
})

$audio.addEventListener('pause', e => {
  e.preventDefault()
  pause()
})

$playButton.addEventListener('click', togglePlaying)
$pauseButton.addEventListener('click', togglePlaying)
$stepBackwardButton.addEventListener('click', stepBackward)
$stepForwardButton.addEventListener('click', stepForward)

$songAnchors.forEach(anchor => {
  anchor.addEventListener('click', changeSong)
})
