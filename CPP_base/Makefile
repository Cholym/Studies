CC=g++
LIBDIR = build
CFLAGS = -std=c++17 -Wall -Wextra -Werror

.PHONY: all clean tests style

STYLE = clang-format --style=google --verbose

all: topic_3 topic_4_2 topic_4_3 topic_5_2 topic_5_3 topic_7_1 topic_7_2

# задание 1.1
topic_3: $(patsubst %.cc, %.o, topic_3.cc)
	@$(CC) $(CFLAGS) topic_3.o -o $@
	@rm -rf *.o

# задание 2.1
topic_4_2: $(patsubst %.cc, %.o, topic_4_2.cc)
	@$(CC) $(CFLAGS) topic_4_2.o -o $@
	@rm -rf *.o

# задание 2.2
topic_4_3: $(patsubst %.cc, %.o, topic_4_3.cc)
	@$(CC) $(CFLAGS) topic_4_3.o -o $@
	@rm -rf *.o

# задание 3.1
topic_5_2: $(patsubst %.cc, %.o, topic_5_2.cc)
	@$(CC) $(CFLAGS) topic_5_2.o -o $@
	@rm -rf *.o

# задание 3.2
topic_5_3: $(patsubst %.cc, %.o, topic_5_3.cc)
	@$(CC) $(CFLAGS) topic_5_3.o -o $@
	@rm -rf *.o

# задание 4.1
topic_7_1: $(patsubst %.cc, %.o, topic_7_1.cc)
	@$(CC) $(CFLAGS) topic_7_1.o -o $@
	@rm -rf *.o

# задание 4.2
topic_7_2: $(patsubst %.cc, %.o, topic_7_2.cc)
	@$(CC) $(CFLAGS) topic_7_2.o -o $@
	@rm -rf *.o

# тест задания 1.1
test_3:
	@chmod +x test_3.sh
	@./test_3.sh

# тест задания 2.1
test_4_2: topic_4_2
	@./topic_4_2
	@./topic_4_2
	@./topic_4_2
	@./topic_4_2

# тест задания 2.2
test_4_3:
	@chmod +x test_4_3.sh
	@./test_4_3.sh

# тест задания 3.1
test_5_2:
	@chmod +x test_5_2.sh
	@./test_5_2.sh

# тест задания 3.2
test_5_3:
	@chmod +x test_5_3.sh
	@./test_5_3.sh

# тест задания 4.1
test_7_1:
	@chmod +x test_7_1.sh
	@./test_7_2.sh

# тест задания 4.2
test_7_2:
	@chmod +x test_7_2.sh
	@./test_7_2.sh

clean:
	@rm -rf topic_3
	@rm -rf topic_4_2
	@rm -rf topic_4_3
	@rm -rf topic_5_2
	@rm -rf topic_5_3
	@rm -rf topic_7_1
	@rm -rf topic_7_2

is_style:
	$(STYLE) -n *.cc

style:
	$(STYLE) -i *.cc