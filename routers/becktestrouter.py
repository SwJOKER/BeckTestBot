from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from questions.beck_test import BeckTest
from keyboards.for_questions import make_row_keyboard, avaible_commands_keyboard
from utils.utils import get_diagnose
from string_vars import *

router = Router()
beck_test = {}

class RouterStates(StatesGroup):
    beck_test = State()


@router.message(Command(commands=['start']))
async def cmd_start(message: types.Message):
    await message.answer(
        WELCOME_MSG
    )


@router.message(Command(commands=['depress']))
async def cmd_start(message: types.Message, state: FSMContext):
    if not message.from_user.id in beck_test:
        beck_test[message.from_user.id] = BeckTest()
    local_beck = beck_test[message.from_user.id]
    next(local_beck.question_generator)
    await message.answer(
        local_beck.current_question,
        reply_markup=make_row_keyboard(local_beck.current_answers_list)
    )
    await state.set_state(RouterStates.beck_test)


@router.message(
    RouterStates.beck_test,
    lambda message: message.text in beck_test[message.from_user.id].current_answers_list
)
async def next_q(message: types.Message, state: FSMContext):
    local_beck = beck_test[message.from_user.id]
    local_beck.add_answer(message.text)
    try:
        next(local_beck.question_generator)
        await message.answer(text=local_beck.current_question,
                             reply_markup=make_row_keyboard(local_beck.current_answers_list))
    except StopIteration:
        await message.answer(text=get_diagnose(local_beck.points), reply_markup=ReplyKeyboardRemove)
        await state.clear()
        del(beck_test[message.from_user.id])


@router.message(
    RouterStates.beck_test,
    lambda message: message.text == EXIT_TEST_MSG
)
async def exit_test(message: types.Message, state: FSMContext):
    await message.answer(text=TEST_INTERRUPTED_MSG, reply_markup=avaible_commands_keyboard())
    await state.clear()


@router.message(
    RouterStates.beck_test,
    lambda message: message.text == TEST_RESTART_MSG
)
async def test_restart(message: types.Message, state: FSMContext):
    del(beck_test[message.from_user.id])
    beck_test[message.from_user.id] = BeckTest()
    local_beck = beck_test[message.from_user.id]
    next(local_beck.question_generator)
    await message.answer(text=TEST_RESTARTED_MSG, reply_markup=avaible_commands_keyboard())
    await message.answer(text=local_beck.current_question,
                         reply_markup=make_row_keyboard(local_beck.current_answers_list))


@router.message()
async def all_other(message: types.Message):
    await message.answer(AVAIBLE_COMMANDS_MSG, reply_markup=avaible_commands_keyboard())


@router.message(RouterStates.beck_test)
async def wrong_message(message: types.Message):
    local_beck = beck_test[message.from_user.id]
    await message.answer(text=WRONG_ANSWER_MSG + '\n\n' +
                              local_beck.current_question,
                         reply_markup=make_row_keyboard(local_beck.current_answers_list))


