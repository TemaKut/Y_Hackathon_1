import React from 'react';

import Style from './Main.module.scss';
import Cell from '../Cell/Cell';
import Button from '../UI/Button/Button';

function Main() {
  return (
    <main className={Style.main}>
      <Cell />
      <Button />
    </main>
  );
}

export default Main;
