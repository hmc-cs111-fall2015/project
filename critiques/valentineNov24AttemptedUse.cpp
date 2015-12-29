#include <SOTR/StateOfTheRobot.h>

DefineStates(MindingManners, PassingButter, Fuming);

interrupt_func([] {
    return justGotInsulted();
}, [] {
    set_state(Fuming);
});

state_func(MindingManners, [] {
    if (justToldToPassButter()) {
        set_state(PassingButter);
    }
});

state_func(PassingButter, [] {
    startFindingButter();
    next_substate();
}, [] {
    if (butterHasBeenFound()) {
        next_substate();
    }
},

[] {
    startPickingUpButter();
    next_substate();
}, [] {
    if (butterHasBeenPickedUp()) {
        next_substate();
    }
},

[] {
    startSendingButter();
    next_substate();
}, [] {
    if (butterHasBeenSent()) {
        next_substate();
    }
});

state_func(Fuming, [] {
    maybeGrumbleABit();
});




