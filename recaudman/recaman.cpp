#include <cstdio>
#include <cstddef>
#include <set>

int main()
{
    std::set<size_t> visited;
    size_t n = 0;
    size_t a = 0;
    
    while (true)
    {
        if (a >= n && visited.find(a - n) == visited.end())
            a -= n;
        else
            a += n;
        visited.insert(a);
        n++;
        putchar(a);
    }
    return 0;
}

