/* eslint-disable prettier/prettier */
import React from 'react';
import { useLocation } from 'react-router-dom';
import Style from './LeftSide.module.scss';


function LeftSide() {
    const location = useLocation();
    const isPackage = ['/package'].includes(location.pathname);
    return (
        // eslint-disable-next-line react/jsx-no-useless-fragment
        <>
            {isPackage ?
                (<container className={Style.container}>
                    <button type='button' className={Style.package}>Слишком маленькая</button>
                    <button type='button' className={Style.package}>Слишком большая</button>
                    <button type='button' className={Style.package}>Нет<br />в наличии</button>
                </container>) :
                (<button type='button' className={Style.problem}>Есть проблема</button>)
            }
        </>
    );
}

export default LeftSide;