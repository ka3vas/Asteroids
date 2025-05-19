# Asteroids v0.0

source venv/bin/activate

## Game loop  proper order:
1. Handle events
2. Clear the screen
3. Update the game state (player.update)
4. Draw the updated state (player.draw)
5. Flip the display to show the new frame
6. Calculate the time delta for the next frame

## What does pygame.display.flip() do?
pygame.display.flip() is a crucial function in Pygame that updates the entire display window with everything that has been drawn to the screen buffer since the last update.

Think of it like this: when you're drawing using functions like screen.fill() or pygame.draw.polygon(), you're actually drawing to a hidden canvas (the screen buffer), not directly to the visible display. The flip() function is what takes that hidden canvas and makes it visible to the player.

Here's what the process looks like:

    You clear the screen with screen.fill("black")
    You draw your game elements with player.draw(screen)
    You call pygame.display.flip() to "flip" the hidden buffer to the visible screen

If you didn't call pygame.display.flip(), nothing you draw would ever become visible to the player. It's similar to the final step of developing a photograph in a darkroom.

There's also a related function called pygame.display.update() which can update just portions of the screen, but flip() is often simpler to use when you're updating the entire display every frame, as most games do.

Does that help clarify what this function does?


    Add a scoring system
    Implement multiple lives and respawning
    Add an explosion effect for the asteroids
    Add acceleration to the player movement
    Make the objects wrap around the screen instead of disappearing
    Add a background image
    Create different weapon types
    Make the asteroids lumpy instead of perfectly round
    Make the ship have a triangular hit box instead of a circular one
    Add a shield power-up
    Add a speed power-up
    Add bombs that can be dropped
