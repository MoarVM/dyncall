#include "dyncall_macros.h"

#if defined(DC__Arch_Intel_x86)
#include "dyncall_callback_x86.c"
#elif defined (DC__Arch_AMD64)
#include "dyncall_callback_x64.c"
#elif defined (DC__Arch_PowerPC)
#include "dyncall_callback_ppc32.c"
#endif
