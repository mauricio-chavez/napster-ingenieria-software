const $playButton = document.querySelector('#play-button')
const $pauseButton = document.querySelector('#pause-button')
const $stepBackwardButton = document.querySelector('#step-backward-button')
const $stepForwardButton = document.querySelector('#step-forward-button')
const $audio = document.querySelector('#audio')
let playing = false

$audio.addEventListener('ended', () => {
  stop()
})

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

$playButton.addEventListener('click', togglePlaying)
$pauseButton.addEventListener('click', togglePlaying)
$stepBackwardButton.addEventListener('click', stepBackward)
$stepForwardButton.addEventListener('click', stepForward)
