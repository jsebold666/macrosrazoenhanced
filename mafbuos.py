//uosteam
if targetexists 'harmful'
  target 'enemy'
  // Harm if enemy is standing next to you
elseif @inrange 'enemy' 1
  cast 'Harm' 'enemy'
else
  if not @findalias 'Sequencing'
    cast 'Magic Arrow' 'enemy'
    @setalias 'Sequencing' 'self'
  else
    cast 'Fireball' 'enemy'
    @unsetalias 'Sequencing'
  endif
  while waitingfortarget 'harmful'
  endwhile
  pause 100
endif