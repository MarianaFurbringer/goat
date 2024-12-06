describe('Player', function() {
  let player;
  let song;

  beforeEach(function() {
    player = new Player();
    song = new Song();
  });

  it('should be able to play a Song', function() {
    player.play(song);
    expect(player.currentlyPlayingSong).toEqual(song);

    // demonstrates use of custom matcher
    expect(player).toBePlaying(song);
  });

  describe('when song has been paused', function() {
    beforeEach(function() {
      player.play(song);
      player.pause();
    });

    it('should indicate that the song is currently paused', function() {
      expect(player.isPlaying).toBeFalsy();

      // demonstrates use of 'not' with a custom matcher
      expect(player).not.toBePlaying(song);
    });

    it('should be possible to resume', function() {
      player.resume();
      expect(player.isPlaying).toBeTruthy();
      expect(player.currentlyPlayingSong).toEqual(song);
    });
  });

  // demonstrates use of spies to intercept and test method calls
  it('tells the current song if the user has made it a favorite', function() {
    spyOn(song, 'persistFavoriteStatus');

    player.play(song);
    player.makeFavorite();

    expect(song.persistFavoriteStatus).toHaveBeenCalledWith(true);
  });

  // demonstrates use of expected exceptions
  describe('#resume', function() {
    it('should throw an exception if song is already playing', function() {
      player.play(song);

      expect(function() {
        player.resume();
      }).toThrowError('song is already playing');
    });
  });
});

console.log("Spec.js loading");

describe("Superlists tests", () => {
  const inputId = "id_text";  
  const errorClass = "invalid-feedback";  
  const inputSelector = `#${inputId}`;  
  const errorSelector = `.${errorClass}`;  
  let testDiv;
  let textInput;  
  let errorMsg;  

  beforeEach(() => {
    console.log("beforeEach");
    testDiv = document.createElement("div");
    testDiv.innerHTML = `
      <form>
        <input
          id="${inputId}"  
          name="text"
          class="form-control form-control-lg is-invalid"
          placeholder="Enter a to-do item"
          value="Value as submitted"
          aria-describedby="id_text_feedback"
          required
        />
        <div id="id_text_feedback" class="${errorClass}">An error message</div>  
      </form>
    `;
    document.body.appendChild(testDiv);
    textInput = document.querySelector(inputSelector);  
    errorMsg = document.querySelector(errorSelector);  
  });


  afterEach(() => {
    testDiv.remove();
  });

  it("check we know how to hide things", () => {
    const errorMsg = document.querySelector(".invalid-feedback");
    errorMsg.style.display = "none";  
    expect(errorMsg.checkVisibility()).toBe(false);  
  });

  it("should render the form with the correct structure", () => {
    const input = document.getElementById("id_text");
    const feedback = document.getElementById("id_text_feedback");

    expect(input).toBeTruthy();
    expect(feedback).toBeTruthy();
    expect(input.getAttribute("aria-describedby")).toBe("id_text_feedback");
  });


  it("sense-check our html fixture", () => {
    expect(errorMsg.checkVisibility()).toBe(true);
  });

  it("error message should be hidden on input", () => {
    initialize(inputSelector, errorSelector);
    textInput.dispatchEvent(new InputEvent("input"));

    expect(errorMsg.checkVisibility()).toBe(false);
  });

  it("error message should not be hidden before input is fired", () => {
    initialize(inputSelector, errorSelector);
    expect(errorMsg.checkVisibility()).toBe(true);
  });
});

