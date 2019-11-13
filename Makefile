##
## EPITECH PROJECT, 2018
## deBruijn
## File description:
## Makefile
##

NAME	=	305construction_2019

NAME_T	=	test_305

SRC	=	app/Main.hs

TEST	=	test/Spec.hs

all:	$(NAME)

$(NAME): $(SRC)
	stack build --copy-bins --local-bin-path .
	mv 305construction-exe $(NAME)

$(NAME_T):	$(TEST)
	stack build --copy-bins --local-bin-path .
	mv 305construction-exe $(NAME_T)



clean:
	stack clean
	rm .stack-work deBruijn.cabal -rf

fclean:	clean
	$(RM) $(NAME)

re:	fclean all

.PHONY:	all clean fclean re
